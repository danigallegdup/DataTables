import pandas as pd
import os
import itertools
import sys


def step2(input_dir, output_dir):
    # List all the files in the directory
    files = os.listdir(input_dir)

    # Group files by topic
    topics = ['anime', 'cereal', 'candy', 'movie']
    conditions = ['bar', 'color', 'plain', 'zebra']

    # Ensure we have all the needed files
    expected_files = [f"{topic}_{condition}.csv" for topic in topics for condition in conditions]
    assert set(expected_files).issubset(set(files)), "Missing files in the input directory"

    # Generate unique combinations
    combinations = list(itertools.permutations(expected_files, 4))

    # Filter combinations to ensure each group starts with the required topic and condition order
    filtered_combinations = []
    for comb in combinations:
        if (comb[0].startswith('anime_') and
            comb[1].startswith('cereal_') and
            comb[2].startswith('candy_') and
            comb[3].startswith('movie_')):
            # Ensure no repetition of condition
            conditions_in_comb = [file.split('_')[1] for file in comb]
            if len(set(conditions_in_comb)) == 4:
                filtered_combinations.append(comb)

    # Save the filtered combinations as new CSV files
    for idx, comb in enumerate(filtered_combinations[:24]):  # Only create the first 24 unique permutations
        combined_df = pd.concat([pd.read_csv(os.path.join(input_dir, file)) for file in comb])
        combined_df.reset_index(drop=True, inplace=True)
        combined_df.to_csv(os.path.join(output_dir, f'group_{idx + 1:02d}.csv'), index=False)

    print("Files created in:", output_dir)

def main():
    if len(sys.argv) == 3:
        main_data_path = sys.argv[1]
        output_dir = sys.argv[2]
        print(main_data_path)
        print(output_dir)
    else:
        print("need more arguments")

    step2(main_data_path, output_dir)

if __name__ == '__main__':
    main()