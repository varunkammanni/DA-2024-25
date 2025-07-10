import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set default Seaborn style for consistent plotting

# Full S&P and FTSE Line Chart
df_spx_ftse_00_10 = pd.read_csv("/varunkammanni/DA-2024-25/python/Data Visualization/Raw files/line_chart_data.csv")  # Load dataset for line chart
df_spx_ftse_00_10["new_date"] = pd.to_datetime(df_spx_ftse_00_10["Date"])  # Convert Date column to datetime
plt.figure(figsize=(20, 8))
plt.plot(df_spx_ftse_00_10["new_date"], df_spx_ftse_00_10["GSPC500"])  # Plot S&P 500 data
plt.plot(df_spx_ftse_00_10["new_date"], df_spx_ftse_00_10["FTSE100"])  # Plot FTSE 100 data
plt.ylabel("Returns", fontsize=12)
plt.xlabel("Date", fontsize=12)
plt.title("S&P and FTSE returns", fontsize=14, weight="bold")
plt.show()

# Filtered S&P and FTSE Line Chart (H2 2008)
df_spx_ftse_H2_08 = df_spx_ftse_00_10[(df_spx_ftse_00_10.new_date >= '2008-07-01') & 
                                       (df_spx_ftse_00_10.new_date <= '2008-12-31')]  # Filter data for H2 2008
plt.figure(figsize=(20, 8))
plt.plot(df_spx_ftse_H2_08["new_date"], df_spx_ftse_H2_08["GSPC500"])  # Plot filtered S&P 500 data
plt.plot(df_spx_ftse_H2_08["new_date"], df_spx_ftse_H2_08["FTSE100"])  # Plot filtered FTSE 100 data
plt.ylabel("Returns", fontsize=12)
plt.xlabel("Date", fontsize=12)
plt.legend(labels=["S&P 500", "FTSE 100"], fontsize=14)  # Add legend with specific labels
plt.title("S&P and FTSE returns", fontsize=14, weight="bold")
plt.show() 