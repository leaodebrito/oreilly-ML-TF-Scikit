# Autor: Bruno Leão de Brito
# Data: 2023-05-01

# Importando bibliotecas
import pandas as pd
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

#Importando arquivos locais
file_path = 'Projeto 1 - Housing/datasets/housing.csv'
housing = pd.read_csv(file_path, sep=',')


#analise de caracteristicas do dataset
housing.info()


housing_valueCounts = housing['ocean_proximity'].value_counts()
print(housing_valueCounts)

describe_housing = housing.describe()
print(describe_housing)

#plotagem de gráficos histograma
#sns.histplot(housing['median_income'])

#plotagem de gráficos de dispersão
#sns.scatterplot(data = housing, x = 'longitude', y = 'latitude', hue = 'median_income', palette = 'viridis', alpha = 0.2)
#plt.show()