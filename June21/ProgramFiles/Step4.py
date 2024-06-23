import pandas as pd
import sys
import os

# Function to create subsets and return them as DataFrames
def create_subsets(file_path):
    df = pd.read_csv(file_path)

    # Define the column ranges for each subset
    column_ranges = {
        'T1_Header': (6, 11),
        'T2_Header': (12, 17),
        'T3_Header': (18, 23),
        'T4_Header': (24, 29),
        'T5_Header': (30, 35)
    }

    subsets = {}
    for header, (start_col, end_col) in column_ranges.items():
        subset_df = df.iloc[:, start_col:end_col + 1]  # +1 because end index is inclusive
        subsets[header] = subset_df

    return subsets

# Function to combine the subsets into one DataFrame with specified headers
def combine_subsets(subsets):
    combined_df = pd.DataFrame()

    for task_num, (header, subset_df) in enumerate(subsets.items(), 1):
        subset_df.columns = [f'T{task_num}_{col_num}' for col_num in range(1, subset_df.shape[1] + 1)]

        # Create a DataFrame to match the new header format
        task_df = pd.DataFrame({
            'Header': subset_df.iloc[:, 0],
            'Column': subset_df.iloc[:, 1],
            'Par': subset_df.iloc[:, 2],
            'Prompt': subset_df.iloc[:, 3],
            'Answer': subset_df.iloc[:, 4],
            'Answer_Column_or_Row': subset_df.iloc[:, 5]
        })

        # Append the task DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, task_df], ignore_index=True)

    return combined_df

# Function to join two DataFrames side by side and save to a new file
def join_csv_left(df1, df2, output_file_path):
    # Join the two DataFrames side by side
    combined_df = pd.concat([df1, df2], axis=1)
    
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(output_file_path, index=False)
    
    print(f"Files have been joined and saved to {output_file_path} successfully.")




def step4(step2_sol_dir, step3_sol_dir, output_dir):
    dir2_files = sorted(os.listdir(step2_sol_dir))
    dir3_files = sorted(os.listdir(step3_sol_dir))

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, (group_file, processed_file) in enumerate(zip(dir2_files, dir3_files), start=1):
        letter = chr(i + 64)
        file_path = os.path.join(step2_sol_dir, group_file)
        processed_file_path = os.path.join(step3_sol_dir, processed_file)
        output_file_path = os.path.join(output_dir, f'Experiment_Permuation_{letter}.csv')

        # Step 1: Create subsets
        subsets = create_subsets(file_path)

        # Step 2: Combine subsets into one DataFrame
        combined_df = combine_subsets(subsets)

        # Step 3: Load another CSV file to be joined
        processed_df = pd.read_csv(processed_file_path)

        # Step 4: Join the combined DataFrame with the processed DataFrame
        join_csv_left(processed_df, combined_df, output_file_path)

    # Removed return statement to allow for processing of all files
    return output_file_path


def main():

    if len(sys.argv) == 4:
        step2_sol_dir =  sys.argv[1]
        step3_sol_dir =sys.argv[2]
        output_dir = sys.argv[3]
       
        # start = 1
        # file_path = f'step2/group_0{start}.csv'
        # processed_file_path = 'step3/processed_group_0{start}.csv'
        # output_file_path = 'step4/permutationa_0{start}.csv'


        step4(step2_sol_dir, step3_sol_dir, output_dir)
    else:
        print("Usage: script.py <input_dir_1> <input_dir_2> <output_dir>")




    

if __name__ == "__main__":
    main()
