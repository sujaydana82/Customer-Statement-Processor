import csv
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import calendar
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to read data from CSV file
def read_csv(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
    except Exception as e:
        logger.error(f"Error reading CSV file '{filename}': {e}")
        return []

# Function to read data from XML file
def read_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return [
            {
                'Reference': record.get('reference'),
                'Account Number': record.find('accountNumber').text,
                'Description': record.find('description').text,
                'Start Balance': float(record.find('startBalance').text),
                'Mutation': float(record.find('mutation').text),
                'End Balance': float(record.find('endBalance').text)
            }
            for record in root.findall('record')
        ]
    except Exception as e:
        logger.error(f"Error reading XML file '{filename}': {e}")
        return []

# Function to validate data
def validate_data(csv_data, xml_data):
    failed_records = []
    references = set()

    for row in csv_data:
        reference = row['Reference']
        if reference in references:
            failed_records.append(row)
        else:
            references.add(reference)
    
    for record in xml_data:
        reference = record['Reference']
        if reference in references:
            failed_records.append(record)
        else:
            references.add(reference)
        
        calculated_end_balance = record['Start Balance'] + record['Mutation']
        if calculated_end_balance != record['End Balance']:
            failed_records.append(record)

    return failed_records

# Function to write failed records to a new CSV file with timestamp
def write_report(failed_records, report_date):
    try:
        fieldnames = failed_records[0].keys()
        month_year = report_date.strftime("%Y%m")
        output_filename = f"validation_report_{month_year}.csv"
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(failed_records)
        logger.info(f"Validation report generated successfully: {output_filename}")
        return output_filename
    except Exception as e:
        logger.error(f"Error writing validation report: {e}")
        return None

# Function to print failed records to console
def print_report(failed_records):
    try:
        if failed_records:
            logger.info("Validation report:")
            for record in failed_records:
                logger.info(record)
        else:
            logger.info("No failed records found.")
    except Exception as e:
        logger.error(f"Error printing validation report: {e}")

# Main function
def main():
    try:
        # Calculate the previous month's date
        today = datetime.now()
        last_month_end = today.replace(day=1) - timedelta(days=1)
        report_date = last_month_end.replace(day=1)

        # Read data from CSV and XML files
        csv_data = read_csv('records.csv')
        xml_data = read_xml('records.xml')
        
        # Validate data
        failed_records = validate_data(csv_data, xml_data)
        
        # Write report to a new CSV file with timestamp
        report_filename = write_report(failed_records, report_date)
        
        # Print report to console
        print_report(failed_records)
        
        if report_filename:
            logger.info("Monthly validation report process completed successfully.")
        else:
            logger.error("Monthly validation report process failed.")
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
