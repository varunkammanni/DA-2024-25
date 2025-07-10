# Loan Data Processing with NumPy

This project demonstrates how to preprocess and analyze loan data using Python and NumPy. The script `Loan_Data_Processed.py` loads raw loan data, cleans and transforms it, handles missing values, encodes categorical variables, and saves a processed dataset for further analysis or machine learning.

## Features

- Loads raw loan data from CSV
- Handles missing values and fills them appropriately
- Splits data into string (categorical) and numeric columns
- Encodes categorical variables (e.g., months, loan status, term, subgrade, state)
- Performs currency conversion using historical EUR-USD rates
- Combines and sorts processed data
- Saves the cleaned and processed data to a new CSV file

## Data Sources

- **Loan Data:** `/varunkammanni/DA-2024-25/python/Others/loan-data.csv`
- **Currency Data:** `/varunkammanni/DA-2024-25/python/Others/EUR-USD.csv`

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install numpy
   ```
2. **Ensure the required CSV files** are present in the specified directory:
   - `/varunkammanni/DA-2024-25/python/Others/loan-data.csv`
   - `/varunkammanni/DA-2024-25/python/Others/EUR-USD.csv`
3. **Run the script:**
   ```bash
   python Loan_Data_Processed.py
   ```
4. **Output:**
   - The processed data will be saved as `/varunkammanni/DA-2024-25/python/Others/loan-data-preprocessed.csv`

## Customization

- You can use your own loan or currency data by replacing the CSV files, as long as the format matches the script's expectations.
- Modify the script to adjust preprocessing steps or add new features as needed.

## License

This project is licensed under the MIT License.
