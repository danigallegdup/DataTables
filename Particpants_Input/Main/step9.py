import os
import pandas as pd

# Define the directories
input_directory = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/step8"
output_directory = "C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Modified_files"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Get list of files
input_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]

def modify_files(input_directory, output_directory, input_files):
    for idx, file_name in enumerate(input_files):
        # Read the input CSV file
        input_file_path = os.path.join(input_directory, file_name)
        df = pd.read_csv(input_file_path)

        # Ensure the column names are stripped of whitespace
        df.columns = df.columns.str.strip()

        # Convert the second column 'Table PNG' values to strings
        df.iloc[:, 1] = df.iloc[:, 1].astype(str)

        # Append 'task2\\T2_' to 'Table PNG' values from lines 17-32 (1-indexed, so 16-31 in 0-indexed)
        df.iloc[16:32, 1] = 'task2\\T2_' + df.iloc[16:32, 1]

        df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: f'"{x}"')

        # Find and capitalize the substring in column 'Prompt' that matches the value in column 9
        for i, row in df.iterrows():
            prompt = str(row['1Prompt'])
            substring = str(row.iloc[8]).strip()
            if substring in prompt:
                prompt = prompt.replace(substring, substring.upper())
                df.at[i, '1Prompt'] = prompt
        

        # Remove the '1' from the start of each column name
        df.columns = [col[1:] if col.startswith('1') else col for col in df.columns]

        # Create the output file name
        output_file_name = f'Participant{chr(65+idx)}_ExperimentPermutations{idx+1}.csv'
        output_file_path = os.path.join(output_directory, output_file_name)

        # Save the modified dataframe to the output file
        df.to_csv(output_file_path, index=False)

# Perform the modifications on the files
modify_files(input_directory, output_directory, input_files)

print(f"Files modified and saved to {output_directory}")
