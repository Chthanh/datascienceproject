from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline

STAGE_NAME = "Data Investigation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.init_data_ingestion()
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise


STAGE_NAME = "Data Validation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.init_data_validation()
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise

STAGE_NAME = "Data Transformation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.init_data_transformation()
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise