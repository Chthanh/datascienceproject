from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation

class DataTransformationPipeline():
    def __init__(self):
        pass

    def init_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()