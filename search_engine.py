import pandas as pd

# Read the CSV file with optimized data types
df = pd.read_csv(
    'business_contracts_dataset.csv', 
    dtype={
        'ContractValue': 'float32', 
        'Jurisdiction': 'category',
        'ContractStatus': 'category',
        'StartDate': 'object',
        'EndDate': 'object',
        'RenewalDate': 'object'
    }
)

# Convert date columns to datetime objects
date_columns = ['StartDate', 'EndDate', 'RenewalDate']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Calculate memory usage before optimization
df_before = pd.read_csv('business_contracts_dataset.csv')
memory_usage_before = df_before.memory_usage(deep=True).sum()

# Calculate memory usage after optimization
memory_usage_after = df.memory_usage(deep=True).sum()

# Print memory usage before and after optimization
print(f"Memory usage before optimization: {memory_usage_before / 1024 ** 2:.2f} MB")
print(f"Memory usage after optimization: {memory_usage_after / 1024 ** 2:.2f} MB")

# Create a dictionary
data_dict = df.set_index('ContractID').T.to_dict('dict')

# Display the first few entries in the dictionary to verify the data
for idx, (key, value) in enumerate(data_dict.items()):
    if idx > 5:  # Adjust this value to display more or fewer entries
        break
    print(f"{key}: {value}")