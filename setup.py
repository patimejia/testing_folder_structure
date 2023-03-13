import os
import csv

def setup():
    """
    Creates the main.py, test.py, README.md, .gitignore, input directory, sample CSV files, and requirements.txt with example code.
    """
    # Define the content of the files using string templates
    main_code = '''\
def greet(name):
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
'''
    test_code = '''\
from main import greet

if __name__ == "__main__":
    print(greet("Alice"))
'''

    readme_content = '''\
# My Project

This is my awesome project! It does some really cool things.

## Usage

To use this project, follow these steps:

1. Install the dependencies.
2. Run the main.py script.
'''

    gitignore_content = '''\
# Ignore compiled Python files
*.pyc

# Ignore the virtual environment directory
venv/

# Ignore CSV data files
*.csv
'''

    # Create the files and directories
    os.makedirs("input", exist_ok=True)
    with open("main.py", "w") as f:
        f.write(main_code)
    with open("test.py", "w") as f:
        f.write(test_code)
    with open("README.md", "w") as f:
        f.write(readme_content)
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    with open("requirements.txt", "w") as f:
        pass

    # Write fake data to sample CSV files
    for i in range(1, 3):
        filename = f"input/samples{i}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Sample ID", "Soil Type", "pH", "Nitrogen", "Phosphorus", "Potassium"])
            for j in range(1, 101):
                writer.writerow([f"Sample{j}", "Sandy loam", round(6.5, 1), round(1.5, 1),
                                 round(1.0, 1), round(0.5, 1)])

    # Print a message to confirm the files were created
    print("Files created: main.py, test.py, README.md, .gitignore, input/samples1.csv, input/samples2.csv")

if __name__ == "__main__":
    setup()
