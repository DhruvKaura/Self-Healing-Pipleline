import json

from app.models.healing_log import HealingLog


class HealingLogRepository:

    @staticmethod
    def create(db, dataset_id, original_columns, generated_mapping):

        healing_log = HealingLog(
            dataset_id=dataset_id,
            original_columns=json.dumps(original_columns),
            generated_mapping=json.dumps(generated_mapping),
        )

        db.add(healing_log)
        db.commit()
        db.refresh(healing_log)

        return healing_log

    @staticmethod
    def get_all(db):

        return db.query(HealingLog).all()
