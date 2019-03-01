import pandas as pd

def load_data_file(filepath):
    Data = pd.read_csv(filepath)
    print(Data.columns)
    Data.head(10)
    return Data