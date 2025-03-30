#!/usr/bin/env python3

import os
import pandas as pd
from tqdm import tqdm
import glob
import argparse

def merge_csv_files(input_dir, output_dir, key_columns, default_values):
    # Check if directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Directory '{input_dir}' does not exist!")
        return
    
    # Get all CSV files in the specified directory and sort them
    csv_files = sorted(glob.glob(os.path.join(input_dir, '*.csv')))
    
    if not csv_files:
        print(f"No CSV files found in directory: {input_dir}")
        return
    
    print(f"Found {len(csv_files)} CSV files to merge.")
    print("Files will be merged in the following order:")
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {os.path.basename(file)}")
    
    # Initialize an empty list to store all dataframes
    all_dataframes = []
    
    # Read and merge all CSV files
    for csv_file in tqdm(csv_files, desc="Merging CSV files"):
        try:
            # Read the CSV file
            df = pd.read_csv(csv_file)
            all_dataframes.append(df)
        except Exception as e:
            print(f"Error reading {csv_file}: {str(e)}")
    
    if not all_dataframes:
        print("No valid CSV files to merge!")
        return
    
    # Concatenate all dataframes
    merged_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Get the column names from the first file
    columns = merged_df.columns.tolist()
    print("\nAvailable columns:", columns)
    
    # Validate key columns
    invalid_columns = [col for col in key_columns if col not in columns]
    if invalid_columns:
        print(f"Error: Invalid columns: {', '.join(invalid_columns)}")
        return
    
    # Fill empty values with defaults
    for col, default in zip(columns, default_values):
        merged_df[col] = merged_df[col].fillna(default)
    
    # Group by key columns and aggregate
    # For numeric columns, we'll sum them
    # For non-numeric columns, we'll take the first non-null value
    agg_dict = {}
    for col in columns:
        if col not in key_columns:
            if pd.api.types.is_numeric_dtype(merged_df[col]):
                agg_dict[col] = 'sum'
            else:
                agg_dict[col] = 'first'
    
    merged_df = merged_df.groupby(key_columns, as_index=False).agg(agg_dict)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the merged dataframe
    output_file = os.path.join(output_dir, 'merged_output.csv')
    merged_df.to_csv(output_file, index=False)
    
    print(f"\nSuccessfully merged {len(csv_files)} files into {output_file}")
    print(f"Total rows in merged file: {len(merged_df)}")
    print(f"Merged based on columns: {', '.join(key_columns)}")

def main():
    parser = argparse.ArgumentParser(description='Merge multiple CSV files with specified columns and default values.')
    parser.add_argument('-i', '--input-dir', default='.',
                      help='Directory containing CSV files (default: current directory)')
    parser.add_argument('-o', '--output-dir', default=None,
                      help='Directory for output file (default: same as input directory)')
    parser.add_argument('-k', '--key-columns', required=True,
                      help='Comma-separated list of columns to merge on')
    parser.add_argument('-d', '--default-values', required=True,
                      help='Comma-separated list of default values for empty cells (in same order as columns)')
    
    args = parser.parse_args()
    
    # If no output directory specified, use the input directory
    if args.output_dir is None:
        args.output_dir = args.input_dir
    
    # Convert comma-separated strings to lists
    key_columns = [col.strip() for col in args.key_columns.split(',')]
    default_values = [val.strip() for val in args.default_values.split(',')]
    
    merge_csv_files(args.input_dir, args.output_dir, key_columns, default_values)

if __name__ == "__main__":
    main() 