import pandas as pd
import numpy as np
#revise csv
import matplotlib as plt
my_df=pd.DataFrame([["biking",68.5,1985,np.nan],["dancing",83.1,1985,3]],columns=["hobby","weight","birthyear","children"],index=["alice","bob"])
print(my_df)
my_df.to_csv("my_df.csv")
my_df_loaded=pd.read_csv("my_df.csv",index_col=0)
print(my_df_loaded)
print("-----------")
data=pd.read_csv("data.csv")
print(data)
print("------------")
print(data.head(n=2))
print("------------")
print(data.tail(n=2))
print("------------")
print(data.info())
print("------------")
print(data.describe())
print("------------")
m=(data.isnull().sum())
print("count null values:",m)
print("------------")

k=data.fillna(130,inplace= True)
print("k:",k)
print("------------")
l=data.fillna(30,inplace=False)
print("l:",l)
print("-----------")

ndf=data.dropna()
print(ndf.isnull().sum())
print(data.isnull().sum())
