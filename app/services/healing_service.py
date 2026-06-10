class HealingService:

    @staticmethod
    def generate_mapping(
        expected_columns,
        actual_columns
    ):

        return {
            "user_id": "id",
            "cost": "price",
            "date_of_purchase": "transaction_date"
        }