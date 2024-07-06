import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import warnings
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle as pk

pt=PorterStemmer()
cv=CountVectorizer(max_features=5000, stop_words='english')

from dataclasses import dataclass
from src.components.data_transformation import DataTransform
warnings.filterwarnings('ignore')

@dataclass
class ModelConfig:
    obj = DataTransform()
    df = obj.transform()

class ModelBuild:
    def __init__(self):
        self.config=ModelConfig()
        self.df = self.config.df

    def stemming(self, text):
        l=[]
        for i in text.split():
            l.append(pt.stem(i))
        return " ".join(l)
    
    def recommend(self, movie, similarity):
        try:
            index = self.df[self.df['title']==movie].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
            for i in distances[1:6]:
                print(self.df.iloc[i[0]].title)

        except Exception as e:
            raise CustomException(e)
    
    def predict(self, movie):
        self.df['tag'] = self.df['tag'].apply(self.stemming)
        vector = cv.fit_transform(self.df['tag']).toarray()
        similarity = cosine_similarity(vector)
        self.recommend(movie, similarity)

obj = ModelBuild()
obj.predict("Skyfall")

        