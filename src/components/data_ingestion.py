import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass

@dataclass
class DataIngestion:
    credits_path: str = 'E:/Krish Naik/notebooks/data/tmdb_5000_credits.csv'
    movies_path: str = 'E:/Krish Naik/notebooks/data/tmdb_5000_movies.csv'

    def data_ingestion(self):
        logging.info('Data Ingestion started')
        try:
            credits = pd.read_csv(self.credits_path)
            movies = pd.read_csv(self.movies_path)
            logging.info('Data Ingestion completed')
            return credits, movies
        except Exception as e:
            logging.error('Error during data ingestion')
            raise CustomException(e)

obj = DataIngestion()
credits, movies = obj.data_ingestion()
