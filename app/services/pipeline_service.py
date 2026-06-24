from app.constants.dataset_status import DatasetStatus
from app.repositories.dataset_repository import DatasetRepository
from app.repositories.healing_log_repository import HealingLogRepository
from app.services.csv_service import CSVService
from app.services.healing_service import HealingService
from app.services.schema_validator import SchemaValidator


class PipelineService:

    @staticmethod
    def process_dataset(file, db):

        # Create Dataset
        dataset = DatasetRepository.create(db=db, filename=file.filename)

        # Dataset Uploaded
        DatasetRepository.update_status(
            db=db, dataset=dataset, status=DatasetStatus.UPLOADED
        )

        try:

            # Validation Started
            DatasetRepository.update_status(
                db=db, dataset=dataset, status=DatasetStatus.VALIDATING
            )

            # Read CSV
            df = CSVService.read_csv(file.file)

            # Extract Columns
            columns = CSVService.get_columns(df)

            # Validate Schema
            validation_result = SchemaValidator.validate(columns)

            mapping = None
            healed_validation = None

            # Heal Schema If Needed
            if not validation_result["valid"]:

                DatasetRepository.update_status(
                    db=db, dataset=dataset, status=DatasetStatus.HEALING
                )

                mapping = HealingService.generate_mapping(
                    expected_columns=SchemaValidator.EXPECTED_SCHEMA,
                    actual_columns=columns,
                )

                healed_df = CSVService.apply_mapping(df=df, mapping=mapping)

                healed_columns = CSVService.get_columns(healed_df)

                healed_validation = SchemaValidator.validate(healed_columns)

                HealingLogRepository.create(
                    db=db,
                    dataset_id=str(dataset.id),
                    original_columns=columns,
                    generated_mapping=mapping,
                )

            # Processing Completed Successfully
            DatasetRepository.update_status(
                db=db, dataset=dataset, status=DatasetStatus.COMPLETED
            )

            return {
                "dataset_id": str(dataset.id),
                "filename": file.filename,
                "original_columns": columns,
                "validation": validation_result,
                "mapping": mapping,
                "healed_validation": healed_validation,
                "status": dataset.status,
            }

        except Exception as e:

            # Processing Failed
            DatasetRepository.update_status(
                db=db, dataset=dataset, status=DatasetStatus.FAILED
            )

            raise e
