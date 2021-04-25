# Environment Variable Diff Tool - `envdiff`

Highlight differences between environment variables in .env files. This tool will compare the two files provided to it and:
- Look for key-value pairs in each file
- Locate unique key-values in each file
- Locate shared key-value pairs between the two files
- Display all unique values in each file, and all shared key-value pairs where the values differ between each file

While it is true that you can use a command like `diff` to compare two env files, it is not always useful because the same environment variables can be set on different lines, which would not be caught using the diff tool. There might also be commented-out lines that you would want to ignore, or lines with comments in them that would be flagged as differences.

### Usage

 - Clone the repo to your local machine

 - Install the dependencies from `requirements.txt`

    ```pip install -r requirements.txt```

 - Run the following command with Python 3:

    ```python3 ./main.py <file_one> <file_two>```

### Test

 - Install the dependencies from `requirements.txt`

    ```pip install -r requirements.txt```

 - Run the following command

    ```python -m unittest discover```
