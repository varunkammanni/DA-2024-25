import pandas as pd

# Load and Inspect Data
raw_csv_data = pd.read_csv("varunkammanni/DA-2024-25/python/Absenteeism/Absenteeism-data.csv")  # Loads the CSV file into a pandas DataFrame.
df = raw_csv_data.copy()  # Creates a copy of the raw data to preserve the original dataset.
type(raw_csv_data)  # Checks the type of the raw_csv_data object (returns DataFrame type, but not used further).

# Drop Unnecessary Columns
df = df.drop(['ID'], axis=1)  # Removes the 'ID' column from the DataFrame as it's not needed for analysis.
df = df.drop(['Reason for Absence'], axis=1)  # Drops the 'Reason for Absence' column after creating dummy variables.

# Process 'Reason for Absence' Column
unique_reasons = pd.unique(df['Reason for Absence'])  # Retrieves unique values in the 'Reason for Absence' column.
num_unique_reasons = len(unique_reasons)  # Counts the number of unique reasons for absence.
reason_counts = raw_csv_data['Reason for Absence'].value_counts()  # Counts occurrences of each reason in the original data.
reason_columns = pd.get_dummies(df['Reason for Absence']).astype(int)  # Creates dummy variables for 'Reason for Absence' and converts to integers.
reason_columns['check'] = reason_columns.sum(axis=1)  # Adds a 'check' column summing dummy variables for each row to verify one-hot encoding.
total_checks = reason_columns['check'].sum(axis=0)  # Sums the 'check' column to verify total number of reasons.
unique_checks = reason_columns['check'].unique()  # Gets unique values in the 'check' column to ensure valid encoding.
reason_columns = pd.get_dummies(df['Reason for Absence'], drop_first=True).astype(int)  # Creates dummy variables, dropping the first category to avoid multicollinearity.

# Group Reason Columns
reason_type_1 = reason_columns.loc[:, 1:14].max(axis=1)  # Groups reasons 1-14 into a single column (max value indicates presence).
reason_type_2 = reason_columns.loc[:, 15:17].max(axis=1)  # Groups reasons 15-17 into a single column.
reason_type_3 = reason_columns.loc[:, 18:21].max(axis=1)  # Groups reasons 18-21 into a single column.
reason_type_4 = reason_columns.loc[:, 22:].max(axis=1)  # Groups reasons 22 and above into a single column.

# Combine Reason Groups with DataFrame
df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis=1)  # Adds grouped reason columns to the DataFrame.
column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
                'Daily Work Load Average', 'Body Mass Index', 'Education',
                'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']  # Defines new column names including reason groups.
df.columns = column_names  # Assigns the new column names to the DataFrame.

# Reorder Columns (Assuming coulmn_names_reordered was meant to be column_names)
df = df[column_names]  # Reorders DataFrame columns to match the defined order.

# Create a Modified Copy of DataFrame
df_reason_mod = df.copy()  # Creates a copy of the DataFrame for further modifications.

# Process 'Date' Column
df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format='%d/%m/%Y')  # Converts 'Date' column to datetime format.

# Extract Month from Date
list_months = []  # Initializes an empty list to store month values.
for i in range(df_reason_mod.shape[0]):  # Iterates over each row in the DataFrame.
    list_months.append(df_reason_mod['Date'][i].month)  # Appends the month of the date to the list.
df_reason_mod['Month Value'] = list_months  # Adds the month values as a new column.

# Extract Day of the Week
def date_to_weekday(date_value):  # Defines a function to return the weekday of a date (though unused due to vectorized operation).
    return date_value.weekday()  # Returns the weekday index (0-6) for a given date.
df_reason_mod['Day of the Week'] = df_reason_mod['Date'].dt.dayofweek  # Adds a column with the weekday index for each date.

# Transform 'Education' Column
df_reason_mod['Education'] = df_reason_mod['Education'].map({1:0, 2:1, 3:1, 4:1})  # Maps education levels (1 to 0, others to 1) to binarize the column.
education_counts = df_reason_mod['Education'].value_counts()  # Counts occurrences of each education level.
unique_education = df_reason_mod['Education'].unique()  # Retrieves unique values in the 'Education' column.

# Final DataFrame
df_cleaned = df_reason_mod.copy()  # Creates a final copy of the modified DataFrame.
df_cleaned.head(5)  # Displays the first 5 rows of the final DataFrame.