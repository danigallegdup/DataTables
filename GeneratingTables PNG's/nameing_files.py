# Define the base structure for the filenames
base_name = "T2_DS{}_{}_{}{}.png"

# Define the groups and their respective labels and counts
groups = [
    ("anime", "color", 4),
    ("cereal", "zebra", 4),
    ("candy", "plain", 4),
    ("movie", "bar", 4)
]

# Initialize the sequence number
sequence_number = 1

# Loop through each group to generate filenames
for group in groups:
    category, label, count = group
    for i in range(1, count + 1):
        # Generate filename
        filename = base_name.format(sequence_number, category, label, i)
        print(filename)
        # Increment the sequence number for the next file
        sequence_number += 1
