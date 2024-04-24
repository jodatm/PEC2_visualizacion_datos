import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
my_variable = np.random.normal(loc=10, scale=5, size=100)

dataset = pd.read_csv("data/salaries.csv")
dataset = dataset.filter(items=['job_title', 'salary'])
dataset = dataset.head(200)

# Plot
sns.swarmplot(y=dataset["job_title"],x=dataset["salary"])
plt.show() # Display the chart
