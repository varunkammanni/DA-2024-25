import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set default Seaborn style for consistent plotting

df_kdnuggets = pd.read_csv("/varunkammanni/DA-2024-25/python/Data Visualization/Raw files/bar_line_chart_data.csv")  # Load dataset for combined chart
fig, ax = plt.subplots(figsize=(10,7))  # Create figure and axis
sns.set_style("white")
ax.bar(df_kdnuggets["Year"], df_kdnuggets["Participants"], color="k")  # Create bar chart for participants
ax.set_ylabel("Number of Participants", weight="bold", fontsize=12)
ax.tick_params(axis="y", width=2, labelsize="large")  # Customize y-axis ticks
ax1 = ax.twinx()  # Create secondary y-axis
ax1.plot(df_kdnuggets["Year"], df_kdnuggets["Python Users"], color="r", marker="D")  # Plot line chart for Python users
ax1.set_ylabel("Python Users", color="#b60000", weight="bold")  # Label secondary y-axis
ax1.tick_params(axis="y", color="#b60000", width=2, labelsize="large")  # Customize secondary y-axis ticks
ax1.set_title("KD Nuggets Survey Python user", fontsize=12, weight="bold")
plt.show()

# Alternative Combined Bar and Line Chart (Old Method)
fig, ax = plt.subplots(figsize=(9, 6))
ax.bar(x=df_kdnuggets["Year"], height=df_kdnuggets["Participants"], color="black")  # Create bar chart
ax1 = ax.twinx()
ax1.plot(df_kdnuggets["Year"], df_kdnuggets["Python Users"])  # Plot line chart
plt.show() 