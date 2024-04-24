import plotly.express as px

import pandas as pd

# Create a dataframe with random values

dataset = pd.read_csv("data/weatherAUS.csv")


dataset1 = dataset[dataset['Date'].astype(str).str[:4]=="2014"]

dataset1['Date'] = dataset1['Date'].astype(str).str[5:7]

dataset1 = dataset1.filter(items=['Date', 'MinTemp'])

dataset1 = dataset1.groupby(['Date']).mean()

print(dataset1)


dataset2 = dataset[dataset['Date'].astype(str).str[:4]=="2015"]

dataset2['Date'] = dataset2['Date'].astype(str).str[5:7]

dataset2 = dataset2.filter(items=['Date', 'MinTemp'])

dataset2 = dataset2.groupby(['Date']).mean()


dataset3 = dataset[dataset['Date'].astype(str).str[:4]=="2016"]

dataset3['Date'] = dataset3['Date'].astype(str).str[5:7]

dataset3 = dataset3.filter(items=['Date', 'MinTemp'])

dataset3 = dataset3.groupby(['Date']).mean()

print(dataset3)


list1 = []
list2 = []
list3 = []

for xs in dataset1.values:
    for x in xs:
        list1.append(x)
        
for xs in dataset2.values:
    for x in xs:
        list2.append(x)
        
for xs in dataset3.values:
    for x in xs:
        list3.append(x)
        

data = pd.DataFrame({

    'Months': ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic',],

    '2014': list1,

    '2015': list2,
    
    '2016': list3,

})


fig = px.area(data, x='Months', y=['2014', '2015', '2016'], title='Stacked Area Chart',
                color_discrete_sequence=['#000000', '#FFFF00', '#800000'])
fig.show()