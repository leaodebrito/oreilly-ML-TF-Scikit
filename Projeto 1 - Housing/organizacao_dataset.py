from caracterizacao_dados import housing
import pandas as pd
import numpy as np
import sklearn  as sk

print(housing.head())

#Separando o dataset em treino e teste
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size = 0.2, random_state=42)