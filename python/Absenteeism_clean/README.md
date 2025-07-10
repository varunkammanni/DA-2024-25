# Absenteeism Data Preprocessing

This script preprocesses absenteeism data from a CSV file, performing data cleaning, feature engineering, and transformation for further analysis.

## Overview
- Cleans and transforms employee absenteeism records
- Engineers new features for analysis
- Outputs a ready-to-use DataFrame for modeling

## Input
- `Absenteeism-data.csv` containing employee absenteeism records
  - Must include columns like `ID`, `Reason for Absence`, `Date`, etc.
  - The `Date` column should be in `DD/MM/YYYY` format

## Output
- A cleaned and transformed DataFrame (`df_cleaned`) with new features

## Key Steps
- Load and copy the dataset to preserve the original
- Drop unnecessary columns (`ID`, `Reason for Absence`)
- Create dummy variables for `Reason for Absence` and group them into four categories
- Convert `Date` to datetime, extract month and weekday features
- Binarize the `Education` column (`1` to `0`, others to `1`)
- Reorganize columns for clarity

## Usage
1. Ensure the CSV file is located at:
   `varunkammanni/DA-2024-25/python/Absenteeism/Absenteeism-data.csv`
2. Run the script in a Python environment with `pandas` installed
3. The final `df_cleaned` DataFrame will be ready for further analysis or modeling

## Notes
- The script assumes the CSV has the required columns
- The `date_to_weekday` function is defined but unused; consider removing it for efficiency