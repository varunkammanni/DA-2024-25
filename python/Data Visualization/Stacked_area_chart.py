import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set default Seaborn style for consistent plotting

df_fuel_engines = pd.read_csv("/varunkammanni/DA-2024-25/python/Data Visualization/Raw files/stacked_area_chart_data.csv")  # Load dataset for stacked area chart
plt.figure(figsize=(8,6))
colors = ["#011638", "#7e2987", "#ef2026"]  # Define colors for stackplot
labels = ["Diesel", "Petrol", "Gas"]  # Define legend labels
plt.stackplot(df_fuel_engines["Year"], df_fuel_engines["Diesel"], df_fuel_engines["Petrol"], 
              df_fuel_engines["Gas"], colors=colors, edgecolor='none')  # Create stacked area chart
plt.xticks(df_fuel_engines["Year"], fontsize=9, rotation=45)  # Set x-axis ticks
plt.legend(labels=labels, loc="upper left")  # Add legend at upper left
plt.ylabel("Number of Cars", fontsize=9)
plt.title("Popularity of Engine Fuel Types (1982 - 2016)", fontsize=14, weight="bold")
sns.despine()  # Remove top and right spines for cleaner look
plt.show() 