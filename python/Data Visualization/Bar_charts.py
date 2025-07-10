import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set default Seaborn style for consistent plotting

# --- Bar Charts ---
# Used Cars Bar Chart
df_used_cars = pd.read_csv("/varunkammanni/DA-2024-25/python/Data Visualization/Raw files/bar_chart_data.csv")  # Load dataset for bar chart
plt.figure(figsize=(9,6))  # Set figure size
plt.bar(x=df_used_cars["Brand"], height=df_used_cars["Cars Listings"], color="b")  # Create bar chart
plt.xticks(rotation=45, fontsize=13)  # Rotate x-axis labels for readability
plt.ylabel("Number of Listings", fontsize=11)  # Label y-axis
plt.xlabel("Brand Names", fontsize=11)  # Label x-axis
plt.title("Cars Listings by Brand", fontsize=16, fontweight="bold")  # Set chart title
plt.show()  # Display the plot
plt.savefig("Used Cars Bar.png")  # Save the plot as an image 