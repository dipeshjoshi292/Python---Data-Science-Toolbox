import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#loading of csv

df= pd.DataFrame([
    ["biking",68.5,1985,np.nan],
    ["Dancing",45.5,1995,3]
    ],
    columns=["hobby","weight","birthyear","children"],
                 index=["alice","bob"])
'''
print(df)
#saving dataframe to csv
df.to_csv("my_df.csv")
#Dataframes - load csv file
df_load = pd.read_csv("my_df.csv",index_col=0)
print("------------")
print(df_load)
'''
'''
df2=pd.read_csv("df2.csv")
print(df2)

data=pd.read_csv("data.csv")
print(data)
print("------------")
'''
print(data.head())
print(data.tail(n=2))
print(data.info())
print(data.describe())

