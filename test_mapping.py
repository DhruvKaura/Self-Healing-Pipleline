from app.services.healing_service import HealingService

mapping = HealingService.generate_mapping(
    expected_columns=[
        "id",
        "price",
        "transaction_date"
    ],
    actual_columns=[
        "user_id",
        "cost",
        "date_of_purchase"
    ]
)

print(mapping)