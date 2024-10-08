from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = 'Prepare base model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f" {STAGE_NAME} has started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} has completed")
    except Exception as e:
        logger.exception(e)
        raise e