from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "TEST"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.init_data_ingestion()
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise

