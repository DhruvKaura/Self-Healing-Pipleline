import pandas as pd

from app.services.csv_service import CSVService


def test_get_columns():

    df = pd.DataFrame({
        "id": [1],
        "price": [100]
    })

    columns = CSVService.get_columns(df)

    assert columns == [
        "id",
        "price"
    ]