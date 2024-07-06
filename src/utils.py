import os
import pickle as pk
import sys
from src.components.model_trainer import ModelBuild
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import pickle as pk
import pandas as pd

@dataclass
class PathConfig:
    df_path = 'src/Artifacts/movie_list.pkl'
    similarity_path = 'src/Artifacts/similarity.pkl'
    directory = 'src/Artifacts'

class Recommendation:
    def __init__(self):
        self.config = PathConfig()
        self.df_path = self.config.df_path
        self.similarity_path = self.config.similarity_path
        self.file_path = self.config.directory

    def createDir(self, file_path):
        os.makedirs(file_path, exist_ok=True)
        
    def model_build(self):
        self.createDir(self.file_path)
        obj = ModelBuild()
        df, similarity = obj.model()
        with open(self.df_path, 'wb') as f1:
            pk.dump(df, f1)
        with open(self.similarity_path, 'wb') as f2:
            pk.dump(similarity, f2)

    def recommend(self, movie, similarity, df):
        try:
            index = df[df['title']==movie].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
            movie_name = []
            movie_id = []
            for i in distances[1:6]:
                movie_name.append(df.iloc[i[0]].title)
                movie_id.append(df.iloc[i[0]].id)
            return movie_id, movie_name
        except Exception as e:
            raise CustomException(e,sys)