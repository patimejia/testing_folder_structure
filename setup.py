import os

def setup():
    """
    Creates the main.py, test.py, README.md, and .gitignore files with example code.
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
'''

    # Create the files
    with open("main.py", "w") as f:
        f.write(main_code)
    with open("test.py", "w") as f:
        f.write(test_code)
    with open("README.md", "w") as f:
        f.write(readme_content)
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)

    # Print a message to confirm the files were created
    print("Files created: main.py, test.py, README.md, .gitignore")

if __name__ == "__main__":
    setup()
