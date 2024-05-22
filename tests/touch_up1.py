import os
import pandas as pd

def rename_and_clean_csv_files(directory, prefix_to_remove):
    for filename in os.listdir(directory):
        if filename.endswith(".csv") and filename.startswith(prefix_to_remove):
            # Rename the file
            new_filename = filename.replace(prefix_to_remove, "", 1)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

            # Read the CSV file, skip the first line, and clean empty rows
            csv_file_path = os.path.join(directory, new_filename)
            with open(csv_file_path, 'r') as file:
                lines = file.readlines()[1:]  # Skip the first line
            
            # Remove lines that contain only commas
            cleaned_lines = [line for line in lines if not all(cell == '' for cell in line.strip().split(','))]
            
            # Write the cleaned data back to the file
            with open(csv_file_path, 'w') as file:
                file.writelines(cleaned_lines)
            print(f"Cleaned {new_filename}")

# Usage example:
directory = 'C:/Users/danig/Documents/GitHub/Research/DataTables/tests'
prefix_to_remove = 'All_128_tables_'
rename_and_clean_csv_files(directory, prefix_to_remove)
