import subprocess

scripts = ["Step0_table_csv.py", ]

# Call each script
for script in scripts:
    subprocess.call(["python", script])