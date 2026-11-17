#filter clean group

import pandas as pd
data = {
    "name" : ["gaurav","mohan","arshdeep","mohit"],
    "marks" : [100,76,87,76],
    "city" : ["haldwani","dehradoon","ranchi","ranikhet"]
}
df=pd.DataFrame(data)
high=df[df["marks"]>=80]
print(high)
sorted_df=df.sort_values("marks",ascending=False)
print(sorted_df)
print(df.isna().sum())  # missing values per column

#fill mising numeric values with median
df["marks"]=df["marks"].fillna(df["marks"].median())

#average marks per city
print(df.groupby("city")["marks"].mean())




