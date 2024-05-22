import os

def delete_csv_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            os.remove(filepath)
            print(f"Deleted {filepath}")

def create_restarting_csv(directory):
    restarting_filepath = os.path.join(directory, 'restarting.csv')
    with open(restarting_filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        # You can add any initial content to the restarting.csv file here if needed
        writer.writerow([''])
    print(f"Created {restarting_filepath}")

# Usage example:
directory = 'C:/Users/danig/Documents/GitHub/Research/DataTables/tests'
delete_csv_files_in_directory(directory)
create_restarting_csv(directory)

