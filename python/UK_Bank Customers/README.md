# UK Bank Customers Data Analysis

## Project Overview
This project analyzes the distribution of UK bank customers by region using the `S6-UK-Bank-Customers.csv` dataset. The workflow includes data cleaning, aggregation, and visualization to provide insights into customer demographics across the UK.

## Dataset
- **Input file:** `S6-UK-Bank-Customers.csv`
- **Columns include:**
  - Customer ID
  - Name, Surname
  - Gender
  - Age
  - Region (England, Scotland, Wales, Northern Ireland)
  - Job Classification
  - Date Joined
  - Balance

## Features
- Cleans the dataset by removing rows with missing values
- Ensures the `Balance` column is numeric
- Aggregates customer counts by region
- Saves the results to a CSV file
- Prints summary statistics to the console

## How to Use
1. **Install dependencies:**
   ```bash
   pip install pandas numpy
   ```
2. **Ensure the dataset file** `S6-UK-Bank-Customers.csv` is in the same directory as the script.
3. **Run the script:**
   ```bash
   python UK_Bank_Customers_Clean.py
   ```

## Output
- **region_counts.csv:** CSV file with the number of customers per region
- **Console output:**
  - Confirmation of saved file
  - Customer counts by region

## Analysis & Visualization
- The script groups customers by region and outputs the distribution.
- (Optional) You can use the output CSV for further visualization (e.g., bar charts) in Python or Excel.

## Notes
- The script assumes the dataset has the required columns and that the `Balance` column may contain non-numeric values.
- Only basic cleaning (missing values, numeric conversion) is performed.
- For more advanced analysis or visualization, see the "Future Enhancements" section.

## Future Enhancements
- Analyze additional variables (e.g., Age, Gender, Job Classification)
- Add statistical summaries (e.g., average balance per region)
- Create visualizations (bar charts, pie charts) using matplotlib or Plotly
- Add interactive dashboards for deeper exploration
