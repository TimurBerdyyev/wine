import pandas as pd

def read_and_clean_excel(file_path):
    df = pd.read_excel(file_path, na_values='', keep_default_na=False)
    df = df.where(pd.notnull(df), ' ') 
    products = df.to_dict('records')
    return products
