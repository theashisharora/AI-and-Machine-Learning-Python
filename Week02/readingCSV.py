import numpy as np
import pandas as pd

titanicf = pd.read_csv(r'C:\Users\ashis\AI-and-Machine-Learning-Python-1\Week02\Titanic-Dataset.csv')



titanicf.drop('Cabin',axis=1,inplace=True)
titanicf.drop('Embarked', axis=1, inplace=True)
titanicf.drop('PassengerId', axis=1, inplace=True)

print(titanicf.info())

print(titanicf.head(5))

print(titanicf[titanicf['Age'].isnull()])

indexAge = titanicf[titanicf['Age'].isnull()].index
titanicf.drop(indexAge, inplace=True)

print(titanicf[titanicf['Age'].isnull()])
print(titanicf.info())

gender = titanicf.replace('male',0,inplace=True)
print(titanicf.info())

print(titanicf.head(5))