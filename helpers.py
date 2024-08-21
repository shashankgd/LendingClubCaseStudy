import pandas as pd


def load_loan_data() -> pd.DataFrame:
    df = pd.read_csv('loan.csv')
    return df
