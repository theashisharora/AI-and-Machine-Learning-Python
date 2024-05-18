import numpy as np
import pandas as pd

labels = ['a','b','c']
values = [1,5,7]
dic = {'a':1,'b':10,'c':50,'d':2}

l1 = pd.Series(data=values)
print(l1)

l2 = pd.Series(data=values, index=labels)
print(l2)

l3 = pd.Series(data=dic)
print(l3)

l4 = l2 + l3
print(l4)