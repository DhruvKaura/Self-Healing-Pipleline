from app.services.schema_validator import SchemaValidator


def test_valid_schema():

    columns = ["id", "price", "transaction_date"]

    result = SchemaValidator.validate(columns)

    assert result["valid"] is True
    assert result["missing_columns"] == []


def test_missing_columns():

    columns = ["user_id", "cost"]

    result = SchemaValidator.validate(columns)

    assert result["valid"] is False
    assert "id" in result["missing_columns"]
