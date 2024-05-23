import pandas as pd
import os

def excel_to_csv(workbook_path):
    # Load the workbook
    xls = pd.ExcelFile(workbook_path)
    
    # Get the directory and base name of the workbook
    workbook_dir = os.path.dirname(workbook_path)
    workbook_name = os.path.basename(workbook_path).split('.')[0]

    # Loop through each sheet and save as a CSV file
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(workbook_path, sheet_name=sheet_name)
        csv_file_path = os.path.join(workbook_dir, f"{workbook_name}_{sheet_name}.csv")
        df.to_csv(csv_file_path, index=False)
        print(f"Saved {csv_file_path}")

# Usage example:
excel_to_csv('C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/main.xlsx')
