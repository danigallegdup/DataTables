"""
From the main dataset, this script creates a set of files, each containing 4 rows of data. The files are grouped by Topic and Condition.

for example, if the main dataset contains the following data:
anime_bar.csv
anime_color.csv
anime_plain.csv
anime_zebra.csv

"""

import argparse
import sys
import pandas as pd
import os

NUM_OF_ROWS = 4

def split_rows_into_4(main_data_path, output_dir):
    # Load the main dataset
    main_data = pd.read_csv(main_data_path)

    # Group by Topic and Condition
    grouped = main_data.groupby(['Topic', 'Condition'])

    file_index = 1

    # Iterate through each group
    for (topic, condition), group in grouped:
        # Sort by Repetition
        group = group.sort_values(by='Repetition')
        
        # Split the group into sets of 4
        for i in range(0, len(group), NUM_OF_ROWS):
            subset = group.iloc[i:i+NUM_OF_ROWS]
            if not subset.empty:
                file_name = f'{topic}_{condition}.csv'
                file_path = os.path.join(output_dir, file_name)
                subset.to_csv(file_path, index=False)
                file_index += 1

    print("Files created in:", output_dir)

def main():
    parser = argparse.ArgumentParser(description='Split rows into sets of 4')
    # Check if any arguments were passed (first argument is the script name itself)
    if len(sys.argv) == 3:
        main_data_path = sys.argv[1]
        output_dir = sys.argv[2]
        print(main_data_path)
        print(output_dir)
    else:
        print("need more arguments")


    split_rows_into_4(main_data_path, output_dir)
if __name__ == '__main__':
    main()