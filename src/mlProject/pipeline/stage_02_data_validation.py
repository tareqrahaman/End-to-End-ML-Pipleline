from mlProject.components.data_validation import DataValidation
from mlProject.config.configuration import ConfigurationManager


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
  def __init__(self):
    pass
  def main(self):
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(data_validation_config)
    data_validation.validate_all_columns()