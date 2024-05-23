import pandas as pd
import os


# Define the iheaders for the new CSV files
headers = [
    "Task_ID", "Table_PNG", "Table Rendering", "Dataset Number", "Topic", "Condition",
    "Repetition", "Task", "Header", "Column", "Par_1", "Prompt", "Expected_Answer", "Answer_Column_or_Row"
]



# Define the input and output directories
input_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step4_taskId'
output_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step5_skeleton'
os.makedirs(output_dir, exist_ok=True)

# List all the files in the directory
files = os.listdir(input_dir)

# Loop through each file and create the modified version
for file in files:
    if file.endswith('.csv'):
        file_path = os.path.join(input_dir, file)
        
        try:
            df = pd.read_csv(file_path)
            
            if not df.empty:
                # Select the first 8 columns
                df = df.iloc[:, :14]
                
                # Save the modified file
                output_file_path = os.path.join(output_dir, file)
                df.to_csv(output_file_path, index=False)
                
        except pd.errors.ParserError as e:
            print(f"Error reading {file_path}: {e}")

print("Files modified and saved in:", output_dir)