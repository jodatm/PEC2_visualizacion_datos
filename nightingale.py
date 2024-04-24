import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# Data
my_variable = np.random.normal(loc=10, scale=5, size=100)

dataset = pd.read_csv("data/avocado.csv")
years = dataset["Date"].astype(str).str[:4].unique()

print(years)
dataset = dataset[dataset['year'] == 2016]
print(dataset.head())
print(dataset.describe())
print(dataset.info())

result = dataset['Date'].astype(str).str[5:7].value_counts().sort_index()

print(result.index)
print(result.values)
