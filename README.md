# Environment Variable Diff Tool - `envdiff`

Highlight differences between environment variables in .env files. While it is true that you can use a command like `diff` to compare two env files, it is not always useful because the same environment variables can be set on different lines, which would not be caught using the diff tool. There might also be commented-out lines that you would want to ignore, or lines with comments in them that would be flagged as differences.

This tool will compare the two files provided to it and:

- Look for **key-value** pairs in each file, while disregarding irrelevant lines (e.g. comments)
- Determine the **unique** key-values in each file
- Determine the **shared** key-value pairs between the two files
- Display all **unique** key-value pairs in each file, as well as all **shared** key-value pairs where the values differ between each file

## Usage

 - Clone the repo to your local machine

 - Install the dependencies from `requirements.txt`

    ```pip install -r requirements.txt```

 - Run the following command with Python 3:

    ```python3 ./main.py <file_one> <file_two>```
    
#### Additional Arguments

You can also customize how the tool interprets your file, as some env files might use different comment characters, or different key-value pair separators. To do this, pass these additional command-line arguments:

 - `-c "<string>"` - `<string>` will be used to determine if a line or substring is a comment or not
 - `-s "<string>"` - `<string>` will be used to separate key-value pairs within each line

## Test

 - Install the dependencies from `requirements.txt`

    ```pip install -r requirements.txt```

 - Run the following command

    ```python -m unittest discover```

## To do
 - [x] Filter out mid-line comments in addition to full-line comments
 - [x] Allow different comment characters and key-value separators via command-line arguments
 - [ ] Release as Python package (?)
 - [ ] Release as command-line installable
