# Import the relevant libraries
import os
from InquirerPy import prompt
from rich.console import Console
from rich.text import Text

# create the readme generator function for initialisation
def readme_generator():
    console = Console()
    console.print(Text("GitHub README Generator", style="bold magenta"))

# Get user input with Inquirer    
    questions = [
        {"type": "input", "name": "project_name", "message": "Project Name:"},
        {"type": "input", "name": "description", "message": "Project Description:"},
        {"type": "input", "name": "installation", "message": "Installation Steps (comma-separated):"},
        {"type": "input", "name": "usage", "message": "Usage Instructions:"},
        {"type": "rawlist", "name": "license", "message": "Choose a license:", "choices": [
        "MIT License", "Apache License 2.0", "GNU GPL v3", "GNU LGPL v3", "Mozilla Public License 2.0", "Creative Commons", "Unlicense" 
        ]},
        {"type": "input", "name": "author", "message": "Author/Contact Info"}
    ]

# Get user answers    
    answers = prompt(questions)

# Display formatted Readme content with Rich    
    readme_content = f"""# {answers['project_name']}

## Description
{answers['description']}

## Installation
```
{answers['installation'].replace(',', '\n')}
```

## Usage
{answers['usage']}


## License
This project is licensed under the {answers['license']}.


## Author
{answers['author']}
"""

# Write the result to a generated readme file with success message   
    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(readme_content)
    
    console.print(Text("README.md has been generated successfully!", style="bold green"))

if __name__ == "__main__":
    readme_generator()
