import os

def format_csv_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            format_csv_file(filepath)

def format_csv_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    # Process lines to add a new line whenever there is a space before a comma
    formatted_lines = []
    for line in lines:
        # Split the line on ' ,'
        parts = line.split(' ,')
        for i in range(len(parts)):
            if i == len(parts) - 1:
                formatted_lines.append(parts[i].strip())
            else:
                formatted_lines.append(parts[i].strip() + ' ,')
    
    # Remove the first comma on the first line
    if formatted_lines and formatted_lines[0].startswith(','):
        formatted_lines[0] = formatted_lines[0][1:].strip()
    
    # Check if the file has more than 33 lines and clear lines starting with `,,,,,`
    if len(formatted_lines) > 29:
        formatted_lines = [line for line in formatted_lines if not line.startswith(',,,,,')]
    
    # Write the formatted lines back to the file
    with open(filepath, 'w') as file:
        for line in formatted_lines:
            file.write(line + '\n')
    print(f"Formatted {filepath}")

# Usage example:
directory = 'C:/Users/danig/Documents/GitHub/Research/DataTables/tests'
format_csv_files_in_directory(directory)



