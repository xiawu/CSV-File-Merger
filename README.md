# CSV File Merger

A Python utility to automatically merge multiple CSV files into a single CSV file.

## Features

- Merges multiple CSV files into a single output file
- Preserves column headers
- Shows progress bar during merging
- Handles different CSV formats and encodings
- Supports custom output filename

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your CSV files in the same directory as the script
2. Run the script:
```bash
python merge_csv.py
```

The script will:
- Automatically detect all CSV files in the current directory
- Merge them into a single file named `merged_output.csv`
- Show a progress bar during the merging process

## Notes

- The script assumes all CSV files have the same structure (same column headers)
- The first file's headers will be used as the reference
- Duplicate rows will be preserved 