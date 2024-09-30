from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f" {STAGE_NAME} has started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} has completed")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = 'Prepare base model'
try:
    logger.info(f" {STAGE_NAME} has started")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} has completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model training'
try:
    logger.info(f" {STAGE_NAME} has started")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} has completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation'
if __name__=='__main__':
    try:
        logger.info(f" {STAGE_NAME} has started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} has completed")
    except Exception as e:
        logger.exception(e)
        raise e