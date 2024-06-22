import os

directory = r"C:/Users/danig/Documents/GitHub/Research/Deep_work/DataTable_Experiment/experiment_package/Results/All_input_files/"

EP = "A"
file_name_template = "Experiment_Permuation_{EP}.csv"

# Get a list of all .csv files in the directory
csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

# Rename each file
for file in csv_files:
    # Create the new file name
    new_file_name = file_name_template.format(EP = EP) 

    # Create the full paths to the old and new files
    old_file_path = os.path.join(directory, file)
    new_file_path = os.path.join(directory, new_file_name)

    # Rename the file
    os.rename(old_file_path, new_file_path)

    # Update EP and PID for the next file
    EP = chr(ord(EP) + 1)