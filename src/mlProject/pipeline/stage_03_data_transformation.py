from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
  def __init__(self):
    pass
  def main(self):
    data_config_manager = ConfigurationManager()
    data_config = data_config_manager.get_data_transformation_configuration()
    data_transformation = DataTransformation(data_config)
    data_transformation.train_test_spliting()