# Data Visualization with Python

This project demonstrates a variety of data visualization techniques using Python's popular libraries: **Pandas**, **Matplotlib**, and **Seaborn**. Each chart type is implemented in its own Python script for clarity and modularity.

## Visualizations Included & Script Organization

- **Bar Chart:**
  - Script: `Bar_charts.py`
  - Visualizes the number of used car listings by brand.
- **Pie Chart:**
  - Script: `Pie_chart.py`
  - Shows the distribution of cars by engine fuel type.
- **Stacked Area Chart:**
  - Script: `Stacked_area_chart.py`
  - Illustrates the popularity of different engine fuel types over time (1982–2016).
- **Line Charts:**
  - Script: `Line_charts.py`
  - S&P 500 and FTSE 100 returns over time, including a focused view for the second half of 2008.
- **Histogram:**
  - Script: `Histogram.py`
  - Displays the distribution of real estate prices.
- **Scatter Plots:**
  - Script: `Scatter_plots.py`
  - Shows the relationship between area and price of California real estate (Matplotlib and Seaborn versions).
- **Combined Bar and Line Chart:**
  - Script: `Combined_bar_line_chart.py`
  - Shows KD Nuggets survey participants and Python users over the years.

## Datasets

All required CSV files are now located in the `Raw files` directory:

- `Raw files/bar_chart_data.csv`
- `Raw files/Pie_chart_data.csv`
- `Raw files/stacked_area_chart_data.csv`
- `Raw files/line_chart_data.csv`
- `Raw files/histogram_data.csv`
- `Raw files/scatter_data.csv`
- `Raw files/bar_line_chart_data.csv`

> **Note:** Each script expects its corresponding CSV file(s) to be in the `Raw files` directory, and uses the absolute path in the code.

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. **Ensure the required CSV files** are present in the `Raw files` directory.
3. **Run the desired script** for the chart type you want to visualize. For example:
   ```bash
   python Bar_charts.py
   python Pie_chart.py
   python Stacked_area_chart.py
   python Line_charts.py
   python Histogram.py
   python Scatter_plots.py
   python Combined_bar_line_chart.py
   ```

Each script will display its respective chart. Some charts will also be saved as image files (e.g., `Used Cars Bar.png`).

## Customization

- You can replace the CSV files with your own data, as long as the column names match those expected in the script.
- Modify chart styles, colors, and labels directly in each script to suit your preferences.

## License

This project is licensed under the MIT License.