from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger


class DataIngestionPipeline():
    def __init__(self):
        pass 

    def init_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


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