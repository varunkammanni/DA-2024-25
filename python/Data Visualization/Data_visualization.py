import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set default Seaborn style for consistent plotting

# --- Bar Charts ---
# Used Cars Bar Chart
df_used_cars = pd.read_csv("bar_chart_data.csv")  # Load dataset for bar chart
plt.figure(figsize=(9,6))  # Set figure size
plt.bar(x=df_used_cars["Brand"], height=df_used_cars["Cars Listings"], color="b")  # Create bar chart
plt.xticks(rotation=45, fontsize=13)  # Rotate x-axis labels for readability
plt.ylabel("Number of Listings", fontsize=11)  # Label y-axis
plt.xlabel("Brand Names", fontsize=11)  # Label x-axis
plt.title("Cars Listings by Brand", fontsize=16, fontweight="bold")  # Set chart title
plt.show()  # Display the plot
plt.savefig("Used Cars Bar.png")  # Save the plot as an image

# --- Pie Chart ---
df_fuel_engine_type = pd.read_csv("Pie_chart_data.csv")  # Load dataset for pie chart
sns.set_palette('colorblind')  # Set colorblind-friendly palette
plt.figure(figsize=(8,6))
plt.pie(df_fuel_engine_type["Number of Cars"], labels=df_fuel_engine_type['Engine Fuel Type'].values, 
        autopct='%.2f%%', textprops={'size': 'x-large', 'fontweight': 'bold', 'rotation': 20})  # Create pie chart with percentage labels
plt.legend()  # Add legend
plt.title('Cars by Engine Fuel Type', fontsize=16, fontweight="bold")
plt.show()

# --- Stacked Area Chart ---
df_fuel_engines = pd.read_csv("stacked_area_chart_data.csv")  # Load dataset for stacked area chart
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

# --- Line Charts ---
# Full S&P and FTSE Line Chart
df_spx_ftse_00_10 = pd.read_csv("line_chart_data.csv")  # Load dataset for line chart
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

# --- Histogram ---
df_real_esate = pd.read_csv("histogram_data.csv")  # Load dataset for histogram
sns.set_style("white")  # Set white background style
plt.figure(figsize=(8,6))
plt.hist(df_real_esate["Price"], bins=8, color="#108A99")  # Create histogram with 8 bins
plt.ylabel("Number of properties", fontsize=12)
plt.xlabel("Price in (000' $)", fontsize=12)
plt.legend(labels=["Price"], fontsize=14)
plt.title("Distribution of Real Estate Prices", fontsize=14, weight="bold")
plt.show()

# --- Scatter Plots ---
# Matplotlib Scatter Plot
df_real_estate_scatter = pd.read_csv("scatter_data.csv")  # Load dataset for scatter plot
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

# --- Combined Bar and Line Chart ---
df_kdnuggets = pd.read_csv("bar_line_chart_data.csv")  # Load dataset for combined chart
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