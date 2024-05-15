# Customer Statement Processor

## Overview

Customer_Statement_Processor.py is a Python script designed to process monthly deliveries of customer statement records provided in CSV and XML formats. The script validates the provided records and generates a report highlighting any inconsistencies or errors found in the data.

## Purpose

The purpose of this script is to automate the validation process of customer statement records received by Rabobank on a monthly basis. By automating this process, the script helps ensure data accuracy and integrity, allowing the bank to identify and address any discrepancies in the provided records efficiently.

## Usage

1. Clone the [repository](https://github.com/sujaydana82/Customer-Statement-Processor) or download the script file (`Customer_Statement_Processor.py`).
2. Ensure Python 3.x is installed on your system.
3. Place the CSV and XML files containing the customer statement records in the same directory as the script.
4. Run the script using the command `python Customer_Statement_Processor.py`.
5. The script will process the provided CSV and XML files, validate the data, and generate a report highlighting any inconsistencies.
6. The validation report will be saved as a CSV file with a filename format of `validation_report_YYYYMM.csv`, where `YYYY` is the year and `MM` is the month the report was generated for.
7. Also the validation report will be displayed in console when run locally.

## Script Functionality

- **Data Reading**: The script reads customer statement records from both CSV and XML files provided in the input directory.
- **Data Validation**: It validates the records by performing the following checks:
  - Ensuring all transaction references are unique.
  - Validating the end balance for each record.
- **Report Generation**: If inconsistencies are found, the script generates a validation report highlighting the failed records.
- **Logging**: Detailed logging is implemented to capture script execution details, including success messages and error handling.
- **Monthly Execution**: The script is designed to run monthly and automatically generate a report for the previous month's data.

## Dependencies

The script has no external dependencies beyond the Python standard library.

## Security Best Practices

The Customer Statement Processor script follows several security best practices to help mitigate potential risks and ensure the integrity and confidentiality of data. These practices include:

1. **Input Validation**: The script validates input data to prevent injection attacks or unexpected behavior due to malformed data. It uses Python's built-in libraries for parsing CSV and XML files, which provide robust input validation capabilities.

2. **File System Security**: Filenames of input CSV and XML files are explicitly specified in the script (`'record.csv'` and `'record.xml'`), reducing the risk of directory traversal attacks or unintended access to sensitive files.

3. **Logging**: Detailed logging is implemented using Python's built-in `logging` module. The script records execution details, including errors, warnings, and informational messages, without exposing sensitive information in plain text.

4. **Secure Coding Practices**: The script follows secure coding practices, such as input validation, output sanitization, and the use of industry-standard libraries for data processing. It minimizes the risk of common vulnerabilities, such as buffer overflows or injection attacks.

5. **Error Handling**: Robust error handling mechanisms are implemented to gracefully handle unexpected conditions and prevent information leakage through error messages. Sensitive information is not exposed in error messages to minimize the risk of information disclosure.

While the script may not address every possible security consideration, it adheres to these best practices to enhance the overall security posture of the application.

