import pandas as pd
import numpy as np

# Loading the CSV data
def load_and_process_data(filename):  # Changed parameter to a proper variable name
    # Reading the CSV file
    df = pd.read_csv(filename)  # Use the parameter variable
    
    # Cleaning data: removing any rows with missing values
    df = df.dropna()
    
    # Converting Balance to numeric, handling any potential errors
    df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')
    
    # Grouping by Region to get customer counts
    region_counts = df['Region'].value_counts()
    
    return df, region_counts

# Function to save processed data
def save_processed_data(region_counts, output_filename="region_counts.csv"):
    region_counts.to_csv(output_filename)
    return output_filename

if __name__ == "__main__":
    filename = "S6-UK-Bank-Customers.csv"
    df, region_counts = load_and_process_data(filename)
    output_file = save_processed_data(region_counts)
    print(f"Processed data saved to {output_file}")
    print("\nCustomer counts by region:")
    print(region_counts)