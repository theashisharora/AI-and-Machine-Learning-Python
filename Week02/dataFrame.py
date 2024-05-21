import numpy as np
import pandas as pd

rowLabels = ['a','b','c']
values1 = np.random.randint(1,20,4)
values2 = np.random.randint(1,20,4)
values3 = np.random.randint(1,20,4)
colLabels = ['x','y','z',0]

multiArr = [values1.tolist(),values2.tolist(),values3.tolist()]

dataframe = pd.DataFrame(data=multiArr, index=rowLabels, columns=colLabels)

print(dataframe)

print(dataframe['x'])

print(dataframe.z)

print()

dataframe['Sum(x+y)'] = dataframe['x']+dataframe['y']

print(dataframe)

dataframe.drop('Sum(x+y)',axis=1,inplace=True)

print(dataframe)

row = [1,2,3,4]

df2 = pd.DataFrame([row],columns=['x','y','z',0], index=['d'])

dataframe = pd.concat([dataframe, df2])

print(dataframe)