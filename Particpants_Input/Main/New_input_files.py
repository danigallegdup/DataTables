import subprocess

scripts = ["Step0_table_csv.py","Step1_make_sets_of_4.py","Step2_make_24_permuations.py", "step3_extend.py", "step4.py", "step5.py", "step6.py", "step7.py", "step8.py", "step9.py"]

# Call each script
for script in scripts:
    subprocess.call(["python", script])