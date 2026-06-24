import pandas as pd


class CSVService:

    @staticmethod
    def read_csv(file):
        return pd.read_csv(file)

    @staticmethod
    def get_columns(df):
        return df.columns.tolist()

    @staticmethod
    def apply_mapping(df, mapping):
        return df.rename(columns=mapping)
