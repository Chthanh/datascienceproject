from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


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
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.init_data_validation()
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise

    STAGE_NAME = "Data Transformation"
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.init_data_transformation()
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise

    STAGE_NAME = "Training Model"
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.init_model_trainer()
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise

    STAGE_NAME = "Model Evaluation"
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} started<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.init_model_evaluation()
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise