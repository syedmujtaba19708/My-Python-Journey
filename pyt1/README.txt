PYTHON JOURNEY — DAY 1
======================

Topic: Introduction to Python, Comments, and Modules

This folder contains two Python files documenting the first day of my Python
learning journey. The exercises introduce comments, built-in modules, external
modules, loops, and basic output.

FILES
-----

1. pyt1main.py
   - Prints a greeting and a joke.
   - Demonstrates a single-line comment.
   - Demonstrates a multi-line string used as a comment/example.
   - Imports and uses the external pyjoke module.
   - Retrieves a joke with pyjoke.get_joke() and prints it.

2. pyt1side.py
   - Prints the poem "Twinkle Twinkle Little Star".
   - Uses a for loop and range() to print the multiplication table of 5.
   - Imports the external requests module and makes an HTTP GET request
     to https://www.example.com.
   - Uses the built-in os module and os.listdir() to display the contents
     of a directory.
   - Includes comments explaining the code.

CONCEPTS PRACTISED
------------------

- Python comments and code documentation
- Importing modules
- Installing external packages with pip
- Printing output with print()
- Variables and function calls
- for loops and the range() function
- Making a basic HTTP request with requests.get()
- Listing directory contents with os.listdir()
- Raw strings for Windows-style file paths

REQUIREMENTS
------------

Python 3
The following external packages:

    pyjoke
    requests

Install them from a terminal with:

    python -m pip install pyjoke requests

The os module is part of Python's standard library, so it does not need
to be installed separately.

HOW TO RUN
----------

Run either file from the terminal:

    python pyt1main.py

    python pyt1side.py

NOTES
-----

- In pyt1side.py, change the directory path passed to os.listdir() to a
  folder that exists on your own computer. The path in the exercise is
  specific to the original computer.
- The requests example uses https://www.example.com. It requires an
  internet connection.
- Run the commands from the directory where the Python files are saved,
  or provide their full paths.

LEARNING SUMMARY
----------------

Day 1 focused on understanding Python comments and modules, then applying
that knowledge through small practical exercises. These files are part of
my ongoing Python learning journey.
