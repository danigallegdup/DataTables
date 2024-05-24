import os
import pandas as pd

def override_task(input2_start, input1_start, input1_file, input2_file, output_file):
    # Read the input CSV files
    df1 = pd.read_csv(input1_file)
    df2 = pd.read_csv(input2_file)

    # Always copy the first 8 columns of input1
    df1_columns = df1.iloc[:, :8]

    # Create a copy of df1 for modifications
    modified_df1 = df1.copy()

    # Extract the relevant rows and columns from df2
    df2_subset = df2.iloc[input2_start:input2_start+16, :6].copy()

    # Ensure data types are compatible
    for col in df2_subset.columns:
        if df2_subset[col].dtype != modified_df1.iloc[input1_start:input1_start+16, -6:].dtypes[col]:
            df2_subset[col] = df2_subset[col].astype(str)

    # Replace the last 6 columns of input1 with columns from input2 starting at input2_start
    modified_df1.iloc[input1_start:input1_start+16, -6:] = df2_subset.values

    # Save the updated dataframe to the output file
    modified_df1.to_csv(output_file, index=False)

# Define directories
input1_dir = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step5_skeleton"
input2_dir = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Divided_t2345"
output_dir = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step7"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def combine_files(input1_dir, input2_dir, output_dir):
    # List all .csv files in the input directories
    input1_files = [f for f in os.listdir(input1_dir) if f.endswith('.csv')]
    input2_files = [f for f in os.listdir(input2_dir) if f.endswith('.csv')]

    # Ensure the same number of files in both directories
    assert len(input1_files) == len(input2_files), "Mismatch in the number of files in input directories"

    for input1_file, input2_file in zip(input1_files, input2_files):
        # Construct the full paths for the input and output files
        input1_file_path = os.path.join(input1_dir, input1_file)
        input2_file_path = os.path.join(input2_dir, input2_file)
        output_file_path = os.path.join(output_dir, f'combined_{input1_file}')

        # Call override_task for each pair of files
        override_task(2, 18, input1_file_path, input2_file_path, output_file_path)
        override_task(19, 34, input1_file_path, input2_file_path, output_file_path)
        override_task(36, 50, input1_file_path, input2_file_path, output_file_path)
        override_task(53, 66, input1_file_path, input2_file_path, output_file_path)

# Combine the files from input1 and input2 directories
combine_files(input1_dir, input2_dir, output_dir)

print(f"Files combined and saved to {output_dir}")

# Example usage of override_task for individual files
# input1_file_path = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step5_skeleton/example_input1.csv"
# input2_file_path = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Divided_t2345/example_input2.csv"
# output_file_path = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step7/combined_example.csv"

# Additional calls to override_task as required
# override_task(2, 18, input1_file_path, input2_file_path, output_file_path)
# override_task(19, 34, input1_file_path, input2_file_path, output_file_path)
# override_task(36, 50, input1_file_path, input2_file_path, output_file_path)
# override_task(53, 66, input1_file_path, input2_file_path, output_file_path)
