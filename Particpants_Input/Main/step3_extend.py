import pandas as pd
import os

# Define the directory containing the group files
input_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step2_groups_of_24'
output_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step3_extended_groups_of_24'
os.makedirs(output_dir, exist_ok=True)

# List all the files in the directory
files = os.listdir(input_dir)

# Loop through each group file and extend its content 4 times
for file in files:
    if file.endswith('.csv'):
        file_path = os.path.join(input_dir, file)
        df = pd.read_csv(file_path)
        
        # Repeat the content 5 times
        extended_df = pd.concat([df] * 5, ignore_index=True)
        
        # Save the extended file
        output_file_path = os.path.join(output_dir, file)
        extended_df.to_csv(output_file_path, index=False)

print("Files extended and saved in:", output_dir)
