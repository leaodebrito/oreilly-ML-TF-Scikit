import pandas as pd
import numpy as np
import urllib
from urllib import request

file_url = 'https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv'
file = 'datasets/housing.csv'

request.urlretrieve(file_url, file)
