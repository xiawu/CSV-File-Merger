# CSV File Merger

A Python utility to automatically merge multiple CSV files into a single CSV file.

## Features

- Merges multiple CSV files into a single output file
- Preserves column headers
- Shows progress bar during merging
- Handles different CSV formats and encodings
- Supports custom output filename
- Command-line interface for easy automation
- Merges rows with same column values
- Handles empty values with default values

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The script can be run with various command-line arguments:

```bash
python merge_csv.py -i /path/to/input/dir -o /path/to/output/dir -k "column1,column2" -d "default1,default2"
```

### Command-line Arguments

- `-i` or `--input-dir`: Directory containing CSV files (default: current directory)
- `-o` or `--output-dir`: Directory for output file (default: same as input directory)
- `-k` or `--key-columns`: Comma-separated list of columns to merge on (required)
- `-d` or `--default-values`: Comma-separated list of default values for empty cells (required)

### Examples

1. Basic usage (using current directory):
```bash
python merge_csv.py -k "ID,Name" -d "0,Unknown"
```

2. Full usage with all options:
```bash
python merge_csv.py -i ./data -o ./output -k "ID,Name" -d "0,Unknown"
```

3. Show help message:
```bash
python merge_csv.py --help
```

## Notes

- The script assumes all CSV files have the same structure (same column headers)
- Files are merged in alphabetical order
- For numeric columns, values are summed when merging rows
- For non-numeric columns, the first non-null value is kept when merging rows
- Empty cells are filled with the specified default values
- The output file is named `merged_output.csv` 