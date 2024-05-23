import pandas as pd
import os

# Load the main dataset
main_data_path = 'C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/main_all_data.csv'
main_data = pd.read_csv(main_data_path)

# Group by Topic and Condition
grouped = main_data.groupby(['Topic', 'Condition'])

# Create a directory to store the split files
output_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/Particpants_Input/Main/Step1_sets_of_4'
os.makedirs(output_dir, exist_ok=True)

file_index = 1

# Iterate through each group
for (topic, condition), group in grouped:
    # Sort by Repetition
    group = group.sort_values(by='Repetition')
    
    # Split the group into sets of 4
    for i in range(0, len(group), 4):
        subset = group.iloc[i:i+4]
        if not subset.empty:
            file_name = f'{topic}_{condition}.csv'
            file_path = os.path.join(output_dir, file_name)
            subset.to_csv(file_path, index=False)
            file_index += 1

print("Files created in:", output_dir)
