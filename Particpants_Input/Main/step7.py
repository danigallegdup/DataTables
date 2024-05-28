import os
import pandas as pd

def read_and_clean_csv(file_path):
    """
    Reads a CSV file into a DataFrame and cleans the column names.
    """
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    return df

def check_column(df, column_name):
    """
    Checks if a column exists in a DataFrame and is in the last 6 columns.
    Raises a ValueError if the checks fail.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")
    if column_name not in df.columns[-6:]:
        raise ValueError(f"Column '{column_name}' not in the last 6 columns of DataFrame")

def override_task(input2_start, input1_start, input1_file, input2_file, output_file):
    """
    Overrides certain rows and columns of the first input file with data from the second input file.
    """
    df1 = read_and_clean_csv(input1_file)
    df2 = read_and_clean_csv(input2_file)

    check_column(df2, '1Header')  # Check '1Header' in df2

    if 'Task' not in df1.columns:
        raise ValueError("Column 'Task' not found in df1")

    # Always copy the first 8 columns of input1
    df1_columns = df1.iloc[:, :8]

    # Create a copy of df1 for modifications
    modified_df1 = df1.copy()

    # Extract the relevant rows and columns from df2
    df2_subset = df2.iloc[input2_start:input2_start+16, :6].copy()

    # Ensure data types are compatible
    for col in df2_subset.columns:
        df2_subset[col] = df2_subset[col].astype(str)
        if col in modified_df1.columns[-6:]:
            modified_df1.iloc[input1_start:input1_start+16, -6:][col] = modified_df1.iloc[input1_start:input1_start+16, -6:][col].astype(str)

    # Replace the last 6 columns of input1 with columns from input2 starting at input2_start
    modified_df1.iloc[input1_start:input1_start+16, -6:] = df2_subset.values

    # Save the updated dataframe to the output file
    modified_df1.to_csv(output_file, index=False)

def combine_files(input1_dir, input2_dir, output_dir):
    """
    Combines CSV files from two input directories and saves the combined files to an output directory.
    """
    input1_files = [f for f in os.listdir(input1_dir) if f.endswith('.csv')]
    input2_files = [f for f in os.listdir(input2_dir) if f.endswith('.csv')]

    assert len(input1_files) == len(input2_files), "Mismatch in the number of files in input directories"

    for input1_file, input2_file in zip(input1_files, input2_files):
        input1_file_path = os.path.join(input1_dir, input1_file)
        input2_file_path = os.path.join(input2_dir, input2_file)
        output_file_path = os.path.join(output_dir, f'combined_{input1_file}')

        try:
            override_task(2, 18, input1_file_path, input2_file_path, output_file_path)
            override_task(19, 34, input1_file_path, input2_file_path, output_file_path)
            override_task(36, 50, input1_file_path, input2_file_path, output_file_path)
            override_task(53, 66, input1_file_path, input2_file_path, output_file_path)
        except Exception as e:
            print(f"Error processing {input1_file} and {input2_file}: {e}")

def main():
    """
    Main function to combine CSV files from two directories.
    """
    input1_dir = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step5_skeleton"
    input2_dir = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Divided_t2345"
    output_dir = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step7"

    os.makedirs(output_dir, exist_ok=True)
    combine_files(input1_dir, input2_dir, output_dir)

    print(f"Files combined and saved to {output_dir}")

if __name__ == "__main__":
    print("Starting Step 7...")
    main()
