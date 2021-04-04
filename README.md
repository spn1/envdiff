# Environment Variable Diff Tool - `envdiff`

Highlight differences between environment variables in .env files. This tool will compare the two files provided to it and:
- Look for key-value pairs in each file
- Locate unique key-values in each file
- Locate shared key-value pairs between the two files
- Display all unique values in each file, and all shared key-value pairs where the values differ between each file

### Usage

Run the following command with Python 3:

```python3 ./src/main.py <file_one> <file_two>```

