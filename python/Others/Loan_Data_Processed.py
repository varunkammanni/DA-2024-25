import numpy as np

# Set print options for NumPy
np.set_printoptions(suppress=True, linewidth=100, precision=2)

# Load and preprocess data
raw_data_np = np.genfromtxt("/varunkammanni/DA-2024-25/python/Others/loan-data.csv", delimiter=';', skip_header=1, autostrip=True)

# Check for missing values
temporary_fill = np.nanmax(raw_data_np) + 1
temporary_mean = np.nanmean(raw_data_np, axis=0)
temporary_stats = np.array([np.nanmin(raw_data_np, axis=0), temporary_mean, np.nanmax(raw_data_np, axis=0)])

# Split columns into strings and numeric
columns_strings = np.argwhere(np.isnan(temporary_mean)).squeeze()
columns_numeric = np.argwhere(np.isnan(temporary_mean) == False).squeeze()

# Re-import dataset
loan_data_strings = np.genfromtxt("/varunkammanni/DA-2024-25/python/Others/loan-data.csv", delimiter=';', skip_header=1, autostrip=True, 
                                 usecols=columns_strings, dtype=np.str)
loan_data_numeric = np.genfromtxt("/varunkammanni/DA-2024-25/python/Others/loan-data.csv", delimiter=';', autostrip=True, skip_header=1, 
                                 usecols=columns_numeric, filling_values=temporary_fill)

# Load column headers
header_full = np.genfromtxt("/varunkammanni/DA-2024-25/python/Others/loan-data.csv", delimiter=';', autostrip=True, 
                           skip_footer=raw_data_np.shape[0], dtype=np.str)
header_strings, header_numeric = header_full[columns_strings], header_full[columns_numeric]

# Checkpoint function
def checkpoint(file_name, checkpoint_header, checkpoint_data):
    np.savez(file_name, header=checkpoint_header, data=checkpoint_data)
    return np.load(file_name + ".npz")

# Process string columns
header_strings[0] = "issue_date"
loan_data_strings[:,0] = np.chararray.strip(loan_data_strings[:,0], "-15")
months = np.array(['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
for i in range(13):
    loan_data_strings[:,0] = np.where(loan_data_strings[:,0] == months[i], i, loan_data_strings[:,0])

# Loan status
status_bad = np.array(['','Charged Off','Default','Late (31-120 days)'])
loan_data_strings[:,1] = np.where(np.isin(loan_data_strings[:,1], status_bad), 0, 1)

# Term
loan_data_strings[:,2] = np.chararray.strip(loan_data_strings[:,2], " months")
header_strings[2] = "term_months"
loan_data_strings[:,2] = np.where(loan_data_strings[:,2] == '', '60', loan_data_strings[:,2])

# Grade and subgrade
for i in np.unique(loan_data_strings[:,3])[1:]:
    loan_data_strings[:,4] = np.where((loan_data_strings[:,4] == '') & (loan_data_strings[:,3] == i),
                                    i + '5', loan_data_strings[:,4])
loan_data_strings[:,4] = np.where(loan_data_strings[:,4] == '', 'H1', loan_data_strings[:,4])
loan_data_strings = np.delete(loan_data_strings, 3, axis=1)
header_strings = np.delete(header_strings, 3)

# Convert subgrade
keys = list(np.unique(loan_data_strings[:,3]))
values = list(range(1, np.unique(loan_data_strings[:,3]).shape[0] + 1))
dict_sub_grade = dict(zip(keys, values))
for i in np.unique(loan_data_strings[:,3]):
    loan_data_strings[:,3] = np.where(loan_data_strings[:,3] == i, dict_sub_grade[i], loan_data_strings[:,3])

# Verification status
loan_data_strings[:,4] = np.where((loan_data_strings[:,4] == '') | (loan_data_strings[:,4] == 'Not Verified'), 0, 1)

# URL
loan_data_strings[:,5] = np.chararray.strip(loan_data_strings[:,5], 
                                          "https://www.lendingclub.com/browse/loanDetail.action?loan_id=")
loan_data_strings = np.delete(loan_data_strings, 5, axis=1)
header_strings = np.delete(header_strings, 5)

# State address
header_strings[5] = "state_address"
loan_data_strings[:,5] = np.where(loan_data_strings[:,5] == '', 0, loan_data_strings[:,5])
states_west = np.array(['WA', 'OR','CA','NV','ID','MT', 'WY','UT','CO', 'AZ','NM','HI','AK'])
states_south = np.array(['TX','OK','AR','LA','MS','AL','TN','KY','FL','GA','SC','NC','VA','WV','MD','DE','DC'])
states_midwest = np.array(['ND','SD','NE','KS','MN',' nontrivialIA','MO','WI','IL','IN','MI','OH'])
states_east = np.array(['PA','NY','NJ','CT','MA','VT','NH','ME','RI'])
loan_data_strings[:,5] = np.where(np.isin(loan_data_strings[:,5], states_west), 1, loan_data_strings[:,5])
loan_data_strings[:,5] = np.where(np.isin(loan_data_strings[:,5], states_south), 2, loan_data_strings[:,5])
loan_data_strings[:,5] = np.where(np.isin(loan_data_strings[:,5], states_midwest), 3, loan_data_strings[:,5])
loan_data_strings[:,5] = np.where(np.isin(loan_data_strings[:,5], states_east), 4, loan_data_strings[:,5])

# Convert strings to integers
loan_data_strings = loan_data_strings.astype(np.int)

# Checkpoint strings
checkpoint_strings = checkpoint("Checkpoint-Strings", header_strings, loan_data_strings)

# Process numeric columns
for i in [1,3,4,5]:
    loan_data_numeric[:,i] = np.where(loan_data_numeric[:,i] == temporary_fill,
                                    temporary_stats[2, columns_numeric[i]], loan_data_numeric[:,i])

# Currency conversion
EUR_USD = np.genfromtxt("/varunkammanni/DA-2024-25/python/Others/EUR-USD.csv", delimiter=',', autostrip=True, skip_header=1, usecols=3)
exchange_rate = loan_data_strings[:,0]
for i in range(1,13):
    exchange_rate = np.where(exchange_rate == i, EUR_USD[i-1], exchange_rate)
exchange_rate = np.where(exchange_rate == 0, np.mean(EUR_USD), exchange_rate)
exchange_rate = np.reshape(exchange_rate, (10000,1))
loan_data_numeric = np.hstack((loan_data_numeric, exchange_rate))
header_numeric = np.concatenate((header_numeric, np.array(['exchange_rate'])))

# Convert to EUR
columns_dollar = np.array([1,2,4,5])
for i in columns_dollar:
    loan_data_numeric = np.hstack((loan_data_numeric, 
                                  np.reshape(loan_data_numeric[:,i] / loan_data_numeric[:,6], (10000,1))))
header_additional = np.array([column_name + '_EUR' for column_name in header_numeric[columns_dollar]])
header_numeric = np.concatenate((header_numeric, header_additional))
header_numeric[columns_dollar] = np.array([column_name + '_USD' for column_name in header_numeric[columns_dollar]])
columns_index_order = [0,1,7,2,8,3,4,9,5,10,6]
header_numeric = header_numeric[columns_index_order]
loan_data_numeric = loan_data_numeric[:,columns_index_order]

# Interest rate
loan_data_numeric[:,5] = loan_data_numeric[:,5]/100

# Checkpoint numeric
checkpoint_numeric = checkpoint("Checkpoint-Numeric", header_numeric, loan_data_numeric)

# Combine datasets
loan_data = np.hstack((checkpoint_numeric['data'], checkpoint_strings['data']))
header_full = np.concatenate((checkpoint_numeric['header'], checkpoint_strings['header']))

# Sort and save
loan_data = loan_data[np.argsort(loan_data[:,0])]
loan_data = np.vstack((header_full, loan_data))
np.savetxt("/varunkammanni/DA-2024-25/python/Others/loan-data-preprocessed.csv", loan_data, fmt='%s', delimiter=',')