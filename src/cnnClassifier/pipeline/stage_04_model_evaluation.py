from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger


STAGE_NAME = 'Model Evaluation'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
            try:
                config = ConfigurationManager()
                eval_config = config.get_evaluation_config()
                evaluation = Evaluation(eval_config)
                evaluation.evaluation()
                # evaluation.log_into_mlflow()

            except Exception as e:
                raise e
            
if __name__=='__main__':
    try:
        logger.info(f" {STAGE_NAME} has started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} has completed")
    except Exception as e:
        logger.exception(e)
        raise e