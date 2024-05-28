import subprocess

# List of script names
scripts = [f"Step{i}.py" for i in range(10)]

# Call each script
for script in scripts:
    subprocess.call(["python", script])