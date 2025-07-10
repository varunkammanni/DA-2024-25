import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set default Seaborn style for consistent plotting

# Matplotlib Scatter Plot
df_real_estate_scatter = pd.read_csv("/varunkammanni/DA-2024-25/python/Data Visualization/Raw files/scatter_data.csv")  # Load dataset for scatter plot
plt.figure(figsize=(12,8))
scatter = plt.scatter(df_real_estate_scatter["Area (ft.)"], df_real_estate_scatter['Price'], 
                      alpha=0.6, c=df_real_estate_scatter['Building Type'], cmap='viridis')  # Create scatter plot with color mapping
plt.legend(*scatter.legend_elements(), loc="upper left", title="Building Type")  # Add legend based on scatter elements
plt.title("Relationship between Area and Price of California Real Estate", fontsize=14, weight="bold")
plt.ylabel("Area (sq.ft)", weight="bold", fontsize=12)
plt.xlabel("Price in (000' $)", fontsize=12)
plt.show()

# Seaborn Scatter Plot
plt.figure(figsize=(12,8))
sns.scatterplot(x="Area (ft.)", y='Price', data=df_real_estate_scatter, 
                palette=['black', 'darkblue', 'purple', 'pink', 'red'], 
                hue='Building Type', s=100)  # Create scatter plot using Seaborn
plt.title("Relationship between Area and Price of California Real Estate", fontsize=14, weight="bold")
plt.ylabel("Area (sq.ft)", weight="bold", fontsize=12)
plt.xlabel("Price in (000' $)", fontsize=12)
plt.show() 