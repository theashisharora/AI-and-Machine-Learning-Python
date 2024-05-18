import numpy as np

newList = [1,2,5,0,10]

list = np.array(newList)
print(list)

list1 = np.arange(1,10)
print(list1)

list3 = np.arange(1,10,2)
print(list3)

list4 = np.random.rand(10)
print(list4)

list5 = np.random.rand(10) * 10
print(list5)

list6 = np.random.rand(4,4)
print(list6)

list7 = np.random.randint(1,100,10)
print(list7)

list8 = list7.max()
print(list8)

list9 = list7.argmax()
print(list9)

list10 = list7.min()
print(list10)

list11 = list7.argmin()
print(list11)

list12 = list7[3]
print(list12)

list13 = list7[2:5]
print(list13)