import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import ast
import numpy as np
import warnings
from dataclasses import dataclass
from src.components.data_ingestion import DataIngestion
warnings.filterwarnings('ignore')

@dataclass
class DataConfig:
    obj=DataIngestion()
    credits, movies=obj.data_ingestion()

class DataTransform:
    def __init__(self):
        self.config=DataConfig()
        self.credits=self.config.credits
        self.movies=self.config.movies
    
    def transform(self):
        df = self.merge()
        df = self.preprocessing(df)
        return df

    def merge(self):
        movie_features = self.movies[['id','title','genres','keywords','overview','production_companies']]
        credits = self.credits.rename(columns={'movie_id':'id'})
        merged_df = pd.merge(movie_features, credits, on=['id','title'])
        merged_df.dropna(inplace=True)
        return merged_df

    def convert(self, text):
        l=[]
        for i in ast.literal_eval(text):
            l.append(i['name'].lower())
        return l
    
    def cast_convert(self, text):
        l = []
        cnt=0
        for i in ast.literal_eval(text):
            if cnt==3:
                break
            l.append(i['name'].lower())
            cnt+=1
        return l
    
    def director(self, text):
        l=[]
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                l.append(i['name'])
                break
        return l
    
    def remSpace(self, text):
        l=[]
        for i in text:
            l.append(i.replace(" ",""))
        return l
    
    def preprocessing(self, df):
        try:
            df['genres'] = df['genres'].apply(self.convert)
            df['keywords'] = df['keywords'].apply(self.convert)
            df['production_companies'] = df['production_companies'].apply(self.convert)
            df['overview'] = df['overview'].apply(lambda x:x.split())
            df['cast'] = df['cast'].apply(self.cast_convert)
            df['crew'] = df['crew'].apply(self.director)

            df['production_companies'] = df['production_companies'].apply(self.remSpace)
            df['keywords'] = df['keywords'].apply(self.remSpace)
            df['cast'] = df['cast'].apply(self.remSpace)
            df['crew'] = df['crew'].apply(self.remSpace)
            df['genres'] = df['genres'].apply(self.remSpace)
            df['overview'] = df['overview'].apply(self.remSpace)

            df['tag'] = df['genres']+df['keywords']+df['overview']+df['production_companies']+df['cast']+df['crew']
            df.drop(columns=['genres','keywords','overview','production_companies','cast','crew'], inplace=True)
            df['tag'] = df['tag'].apply(lambda x:" ".join(x))

            return df
        
        except Exception as e:
            raise CustomException(e)



