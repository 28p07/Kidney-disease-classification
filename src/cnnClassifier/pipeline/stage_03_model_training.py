from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger

STAGE_NAME = 'Model training'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()

        except Exception as e:
            raise e 

if __name__=='__main__':
    try:
        logger.info(f" {STAGE_NAME} has started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} has completed")
    except Exception as e:
        logger.exception(e)
        raise e