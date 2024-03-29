# Autor: Bruno Leão de Brito
# Data: 2023-05-01

# Objetivo: Obtenção de dados de um arquivo csv a partir de uma url

# Importando bibliotecas
import pandas as pd
import numpy as np
import urllib
from urllib import request

#URL do arquivo
file_url = 'https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv'

#Local onde o arquivo será salvo
file = 'datasets/housing.csv'

#Método para baixar o arquivo
request.urlretrieve(file_url, file)

