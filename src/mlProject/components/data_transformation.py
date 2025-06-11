import os
from mlProject import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
  def __init__(self, config: DataTransformationConfig):
    self.config = config

    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

  def train_test_spliting(self):
    data = pd.read_csv(self.config.data_file)

    #divides train = 0.75 and test = 0.25 
    train, test = train_test_split(data)
    train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
    test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

    logger.info("Splited data into training and test sets.")
    logger.info(f"Train data shape: {train.shape}")
    logger.info(f"Test data shape: {test.shape}")