# Import necessary libraries
import openpyxl
import csv

# Define the function to convert Excel workbook to CSV files
def excel_to_csv(file_name):
    # Load the workbook
    wb = openpyxl.load_workbook(file_name)

    # Iterate through each sheet in the workbook
    for sheet in wb.worksheets:
        # Define the CSV file name
        csv_file_name = f"{sheet.title}.csv"

        # Create a new CSV file with the same name as the sheet
        with open(csv_file_name, 'w', newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)

            # Iterate through each row in the sheet
            for row in sheet.iter_rows(values_only=True, max_col=15):
                # Write the row to the CSV file
                csv_writer.writerow(row)

# Define the name of the Excel file to convert
excel_file_name = "input_participant_files.xlsx"

# Call the function to convert the Excel file to CSV files
excel_to_csv(excel_file_name)