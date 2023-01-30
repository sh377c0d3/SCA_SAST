import subprocess
import csv

code_dir = "code"

# Run the SAST scan using the Bandit tool
output = subprocess.run(["bandit", "-r", code_dir], capture_output=True, text=True)

# Store the results in a CSV file
filename = "sast_results.csv"
with open(filename, "w", newline='') as file:
    writer = csv.writer(file)
    for line in output.stdout.split("\n"):
        if ":" in line:
            writer.writerow(line.split(":"))

