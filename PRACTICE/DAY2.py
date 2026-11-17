#indexing,slicing ,vector math
'''import numpy as np
a=np.array([10,20,30,40,50])
print(a[0])
print(a[1:4])
print(a*2)
print(a+5)
m=np.array([[70,80],[90,60],[85,95]])
print(m.shape)
print(m[0,1])
print(m.mean(axis=0))'''


#Pandas 
#DataFrame basics

import pandas as pd
data = {
    "name" : ["gaurav","mohan","arshdeep","mohit"],
    "marks" : [100,76,87,76],
    "city" : ["haldwani","dehradoon","ranchi","ranikhet"]
}
df=pd.DataFrame(data)
print(df.head())
print(df.shape,df.columns)
print(df.info())
print(df.describe())
print(df["marks"])
print(df.iloc[0])






