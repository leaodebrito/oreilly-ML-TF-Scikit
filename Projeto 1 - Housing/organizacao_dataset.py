# Autor: Bruno Leão de Brito
# Data: 2023-05-01

# Importando bibliotecas
import pandas as pd
import numpy as np
import sklearn  as sk

#Importando arquivos locais
file_path = 'Projeto 1 - Housing/datasets/housing.csv'
housing = pd.read_csv(file_path, sep=',')

#Separando o dataset em treino e teste
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size = 0.2, random_state=42)

print(train_set.head())
print(test_set.head())

#Salvando datasets de treino e teste em arquivos csv
train_set.to_csv('Projeto 1 - Housing/datasets/train_set_housing.csv', index=False)
test_set.to_csv('Projeto 1 - Housing/datasets/test_set_housing.csv', index=False)