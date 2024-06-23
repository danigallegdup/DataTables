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

def call_step4(input_dir_1, input_dir_2, output_directory):
    # Construct the command to call Step1.py with input and output directories
    command = f"python ProgramFiles/Step4.py {input_dir_1} {input_dir_2} {output_directory}"
    
    # Execute the command
    subprocess.run(command, check=True, shell=True) 

HOME_DIR = 'C:/Users/danig/Documents/GitHub/Research/DataTables/June21'

input_dir = f'{HOME_DIR}/InputFile.csv'
step1_output_dir = f'{HOME_DIR}/ProgramFiles/step1'
os.makedirs(step1_output_dir, exist_ok=True)
call_step1(input_dir, step1_output_dir)

input_dir = f'{HOME_DIR}/ProgramFiles/step1'
step2_output_dir = f'{HOME_DIR}/ProgramFiles/step2'
os.makedirs(step2_output_dir, exist_ok=True)
call_step2(input_dir, step2_output_dir)

input_dir = step2_output_dir
step3_output_dir = f'{HOME_DIR}/ProgramFiles/step3'
os.makedirs(step3_output_dir, exist_ok=True)
call_step3(input_dir, step3_output_dir)

input_dir_1 = step2_output_dir
input_dir_2 = step3_output_dir 
step4_output_dir = f'{HOME_DIR}/ProgramFiles/step4'
os.makedirs(step4_output_dir, exist_ok=True)
call_step4(input_dir_1, input_dir_2, step4_output_dir)


