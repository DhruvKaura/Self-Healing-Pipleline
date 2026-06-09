class SchemaValidator:

    EXPECTED_SCHEMA = [
        "id",
        "price",
        "transaction_date"
    ]

    @classmethod
    def validate(cls, incoming_columns):

        missing_columns = [
            column
            for column in cls.EXPECTED_SCHEMA
            if column not in incoming_columns
        ]

        return {
            "valid": len(missing_columns) == 0,
            "missing_columns": missing_columns
        }