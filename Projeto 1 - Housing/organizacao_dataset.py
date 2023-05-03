# Autor: Bruno Leão de Brito
# Data: 2023-05-01

# Objetivo: Organização de dataset para treinamento de modelos de machine learning

# Importando bibliotecas
import pandas as pd
import numpy as np
import sklearn  as sk
from sklearn.model_selection import train_test_split


#Importando arquivos locais
file_path = 'Projeto 1 - Housing/datasets/housing.csv'
housing = pd.read_csv(file_path, sep=',')

#criação de identificador único para cada linha
housing['id'] = housing['longitude'] * 1000 + housing['latitude']

#Separando o dataset em treino e teste
train_set, test_set = train_test_split(housing, test_size = 0.2, random_state=42)

print(train_set.head())
print(test_set.head())

#Salvando datasets de treino e teste em arquivos csv
train_set.to_csv('Projeto 1 - Housing/datasets/train_set_housing.csv', index=False)
test_set.to_csv('Projeto 1 - Housing/datasets/test_set_housing.csv', index=False)
