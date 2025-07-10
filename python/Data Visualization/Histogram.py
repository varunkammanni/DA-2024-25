import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set default Seaborn style for consistent plotting

df_real_esate = pd.read_csv("/varunkammanni/DA-2024-25/python/Data Visualization/Raw files/histogram_data.csv")  # Load dataset for histogram
sns.set_style("white")  # Set white background style
plt.figure(figsize=(8,6))
plt.hist(df_real_esate["Price"], bins=8, color="#108A99")  # Create histogram with 8 bins
plt.ylabel("Number of properties", fontsize=12)
plt.xlabel("Price in (000' $)", fontsize=12)
plt.legend(labels=["Price"], fontsize=14)
plt.title("Distribution of Real Estate Prices", fontsize=14, weight="bold")
plt.show() 