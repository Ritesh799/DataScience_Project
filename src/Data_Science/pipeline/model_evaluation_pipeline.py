from src.Data_Science.config.configuration import ConfigurationManager
from src.Data_Science.components.model_evaluation import ModelEvaluation
from src.Data_Science import logger

STAGE_NAME = "Model Evaluate stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluate_config = config.get_model_evaluation_config()
        model_evaluate = ModelEvaluation(config=model_evaluate_config)
        model_evaluate.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e