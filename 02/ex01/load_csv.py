import pandas as pd

def load(path: str) -> pd.DataFrame: #(You have to adapt the type of return according to your library)
    return pd.read_csv(path)
