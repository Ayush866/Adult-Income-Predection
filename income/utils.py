import pandas as pd
from income.logger import logging
from income.exception import CustomException
from income.config import mongo_client

def get_collection_as_dataframe(database_name:str,collection_name:str) -> pd.DataFrame:
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise CustomException(e, sys)