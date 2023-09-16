import pandas as pd

def load_data():
    # Read the CSV file with optimized data types
    df = pd.read_csv(
        'C:/Users/colto/OneDrive/Desktop/startup/search_engine/business_contracts_dataset.csv',
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

    # Create a dictionary
    data_dict = df.set_index('ContractID').T.to_dict('dict')
    
    return data_dict