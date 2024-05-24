import os
import pandas as pd

# Define the directories
path1 = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step5_skeleton"
path2 = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Divided_t2345"
output_path = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/step8"

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Get list of files
path1_files = [f for f in os.listdir(path1) if f.endswith('.csv')]
path2_files = [f for f in os.listdir(path2) if f.endswith('.csv')]

# Ensure both directories have the expected number of files
assert len(path1_files) == len(path2_files), "Mismatch in the number of files in input directories"

for file1, file2 in zip(path1_files, path2_files):
    # Construct full file paths
    file1_path = os.path.join(path1, file1)
    file2_path = os.path.join(path2, file2)
    output_file_path = os.path.join(output_path, f'merged_{file1}')

    # Read the CSV files
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Strip whitespace from headers to ensure compatibility
    df1.columns = df1.columns.str.strip()
    df2.columns = df2.columns.str.strip()

    # Merge the dataframes side by side
    merged_df = pd.concat([df1, df2], axis=1)

    # Save the merged dataframe to the output file
    merged_df.to_csv(output_file_path, index=False)

print(f"Files merged and saved to {output_path}")
