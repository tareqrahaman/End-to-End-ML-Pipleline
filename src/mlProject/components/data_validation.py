from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
  def __init__(self, config: DataValidationConfig):
    self.config = config
  
  def validate_all_columns(self) -> bool:
    try:
      validation = None

      data = pd.read_csv("artifacts\data_ingestion\winequality-red.csv")
      all_cols = list(data.columns)
      all_schema = self.config.all_schema.keys()
      for col in all_cols:
        if col not in all_schema:
          validation = False
          with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation Status: {validation}")
        else:
          validation = True
          with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation Status: {validation}")
      return validation
    except Exception as e:
      raise e