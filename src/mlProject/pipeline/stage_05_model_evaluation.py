from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager

class ModelEvalutaionTrainingPipeline:
  def __init__(self):
    pass

  def main(self):
    config = ConfigurationManager()
    model_evaluation_config = config.get_model_evaluation_config()
    model_evaluation = ModelEvaluation(model_evaluation_config)
    model_evaluation.save_results()