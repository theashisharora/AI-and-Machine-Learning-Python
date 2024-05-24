import numpy as np
import pandas as pd

ds=pd.read_csv(r'C:\Users\ashis\AI-and-Machine-Learning-Python-2\Exercise\ds_salaries.csv')
print(ds.head())

print(ds.nunique())

CanDF = ds[ds['employee_residence'] == 'CA']

minSal = CanDF['salary']
print()
print(min(minSal))
print(max(minSal))
print(minSal.mean())

display = CanDF[CanDF['salary'] == CanDF['salary'].min()]
display2 = CanDF[CanDF['salary'] == CanDF['salary'].max()]

print(display['salary'])
print(display2['salary'])