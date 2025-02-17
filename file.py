# Import the relevant libraries
from InquirerPy import prompt
from rich.console import Console
from rich.progress import Progress
from rich.text import Text
import time

# Initialise console
console = Console()
console.print(Text("GitHub README Generator", style="bold magenta"))

# Get user input with Inquirer
questions = [
        {"type": "input", "name": "Project Title", "message": "Project Title:"},
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
   
readme_content = f"""

## Project Title 
```
{answers['Project Title']}
```

## Description
```
{answers['description']}
```

## Installation
```
{answers['installation'].replace(',', '\n')}
```

## Usage
```
{answers['usage']}
```


## License
```
This project is licensed under the {answers['license']}.
```

## Author
```
{answers['author']}
```
"""

# Display the readme file content
console.print(readme_content)

# Show a progress bar
with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for _ in range(10):
        time.sleep(0.3)
        progress.update(task, advance=10)

console.print("[bold green]README.md has been generated successfully![/bold green] ✅")