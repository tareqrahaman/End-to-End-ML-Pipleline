from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager

class ModelTrainerTrainingPipeline:
  def __init__(self):
    pass

  def main(self):  
    config_manager = ConfigurationManager()
    model_trainer_config = config_manager.get_model_trainer_config()
    model_trainer = ModelTrainer(model_trainer_config)
    model_trainer.train()