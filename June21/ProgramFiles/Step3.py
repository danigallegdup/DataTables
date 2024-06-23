import os
import csv
import sys



def task1(taskID, file_path, header1, header7, Tasks, itteration):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if itteration == 0:
                new_row = [header1] + row[:6] + [header7]   
                itteration += 1
                if taskID == 1:
                    data.append(new_row)
            else:
                # Construct the new row
                new_row = [taskID] + row[:6] + [Tasks[taskID-1]]
                data.append(new_row)
                # Increment taskID for each row
        return data 

def step3(input_dir, output_dir):
    # Ensure output_dir exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    header1 = "Task ID"
    header7 = "Task"

    taskID = 1
    Tasks =["Filter", "Correlation", "Sort", "Estimate Average","Retrieve Value"]

    itteration = 0

    # List all files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        # Check if it's a file
        if os.path.isfile(file_path):
            data= task1(taskID, file_path, header1, header7, Tasks, itteration)
            data1= task1(2, file_path, header1, header7, Tasks, itteration)
            data2= task1(3, file_path, header1, header7, Tasks, itteration)
            data3= task1(4, file_path, header1, header7, Tasks, itteration)
            data4= task1(5, file_path, header1, header7, Tasks, itteration)
            # Write the processed data to a new file in output_dir

            if data:
                output_file_path = os.path.join(output_dir, f"processed_{filename}")
                with open(output_file_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                    writer.writerows(data1)
                    writer.writerows(data2)
                    writer.writerows(data3)
                    writer.writerows(data4)

                print(f"Processed {filename} and saved to {output_file_path}")
            else:
                print(f"No valid data in {filename} to process")

            
          

def step4():
    pass

def main():
    if len(sys.argv) == 3:
        main_data_path = sys.argv[1]
        output_dir = sys.argv[2]
        data = step3(main_data_path, output_dir)
        print(data)
    else:
        print("Usage: script.py <input_dir> <output_dir>")


if __name__ == '__main__':
    main()
