import pandas as pd


class CSVService:

    @staticmethod
    def get_columns(file):
        df = pd.read_csv(file)

        return df.columns.tolist()