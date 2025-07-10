import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set default Seaborn style for consistent plotting

df_fuel_engine_type = pd.read_csv("/varunkammanni/DA-2024-25/python/Data Visualization/Raw files/Pie_chart_data.csv")  # Load dataset for pie chart
sns.set_palette('colorblind')  # Set colorblind-friendly palette
plt.figure(figsize=(8,6))
plt.pie(df_fuel_engine_type["Number of Cars"], labels=df_fuel_engine_type['Engine Fuel Type'].values, 
        autopct='%.2f%%', textprops={'size': 'x-large', 'fontweight': 'bold', 'rotation': 20})  # Create pie chart with percentage labels
plt.legend()  # Add legend
plt.title('Cars by Engine Fuel Type', fontsize=16, fontweight="bold")
plt.show() 