import os

"""


"""

def rename_files(directory, prefix):
    for filename in os.listdir(directory):
        new_filename = prefix + filename
        source = os.path.join(directory, filename)
        destination = os.path.join(directory, new_filename)
        
        os.rename(source, destination)

# Usage
rename_files('path_to_your_directory', 'new_')