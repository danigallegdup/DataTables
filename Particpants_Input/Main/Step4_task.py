import pandas as pd
import os

# Define the directory containing the group files and the output directory
input_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step3_extended_groups_of_24'
output_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step4_taskId'
os.makedirs(output_dir, exist_ok=True)


# List all the files in the directory
files = os.listdir(input_dir)

# Define the task names and variables
task_names = ["Filter", "Correlation", "Sort", "Estimate Average", "Retrieve Value"]
task_id_variable = [1, 2, 3, 4, 5]

# Loop through each group file and modify the tasks and task IDs
for file in files:
    if file.endswith('.csv'):
        file_path = os.path.join(input_dir, file)
        
        try:
            df = pd.read_csv(file_path)
            
            if not df.empty:
                # Extend the DataFrame with task IDs and task names
                num_rows = len(df)
                df['task id'] = [task_id_variable[i // 16] for i in range(num_rows)]
                df['Task'] = [task_names[i // 16] for i in range(num_rows)]
                
                # Save the modified file
                output_file_path = os.path.join(output_dir, file)
                df.to_csv(output_file_path, index=False)
                
        except pd.errors.ParserError as e:
            print(f"Error reading {file_path}: {e}")

print("Files modified and saved in:", output_dir)