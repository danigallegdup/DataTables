import subprocess
import os

def call_step1(input_directory, output_directory):
    # Construct the command to call Step1.py with input and output directories
    command = f"python ProgramFiles/Step1.py {input_directory} {output_directory}"
    
    # Execute the command
    subprocess.run(command, check=True, shell=True)

def call_step2(input_directory, output_directory):
    # Construct the command to call Step1.py with input and output directories
    command = f"python ProgramFiles/Step2.py {input_directory} {output_directory}"
    
    # Execute the command
    subprocess.run(command, check=True, shell=True) 

def call_step3(input_directory, output_directory):
    # Construct the command to call Step1.py with input and output directories
    command = f"python ProgramFiles/Step3.py {input_directory} {output_directory}"
    
    # Execute the command
    subprocess.run(command, check=True, shell=True) 



input_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/June21/InputFile.csv'
step1_output_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/June21/ProgramFiles/step1'
os.makedirs(step1_output_dir, exist_ok=True)
call_step1(input_dir, step1_output_dir)

input_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/June21/ProgramFiles/step1'
step1_output_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/June21/ProgramFiles/step2'
os.makedirs(step1_output_dir, exist_ok=True)
call_step2(input_dir, step1_output_dir)

input_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/June21/ProgramFiles/step2'
step1_output_dir = 'C:/Users/danig/Documents/GitHub/Research/DataTables/June21/ProgramFiles/step3'
os.makedirs(step1_output_dir, exist_ok=True)
call_step3(input_dir, step1_output_dir)


