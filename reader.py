import pandas as pd


def excel_file(file_path):
    df = pd.read_excel(file_path)
    data = df.to_dict(orient='records')
    print(data)
    return data