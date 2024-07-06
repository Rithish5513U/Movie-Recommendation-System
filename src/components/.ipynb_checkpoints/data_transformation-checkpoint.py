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


