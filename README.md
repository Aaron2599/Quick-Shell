[![PyPI - Version](https://img.shields.io/pypi/v/quickshell)](https://pypi.org/project/quickshell/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)


# QuickShell: Simplify Shell Command Execution in Python

## Overview

QuickShell is a simple Python library designed to remove the boilerplate when dealing with shell commands.

## Key Features

- **Asynchronous Execution**: Run shell commands asynchronously using asyncio.
- **Flexible Output Handling**: Easily print and capture command output and errors.

## Installation

Get started with QuickShell by installing it via pip:

```sh
pip install quickshell
```

## Usage
use QuickShell to quickly run a command:
```python
import asyncio
from quickshell import run_shell

async def main():
    cmd = 'echo Hello from the shell!'
    stdout, stderr = await run_shell(cmd, print_output=True) # Output: Hello from the shell!
    
if __name__ == '__main__':
    asyncio.run(main())
```

# Explanation
- **Importing the Library:** the `run_shell` function is imported from the `quickshell` library.
- **Define the Command:** Replace `"dir"` with the shell command you want to execute.
- **Running the Command:** The `run_shell` function executes the command asynchronously and captures its output.
- **Printing the Output:** Set `print_output=True` to print the live output and errors from the shell.