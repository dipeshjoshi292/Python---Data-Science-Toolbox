import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''s = pd.Series([1,-2,6,7])
print(np.square(s))
print(s)
#arithmetic 
a = s+[1000,2000,3000,4000]
print(a)
print(s+1000)
print(s<0)



c = np.arange(24).reshape(2,3,4)
print(c)
print(c.sum(axis=0))


e = pd.Series([99,98,56,45],index=["a","b","c","d"],name="haha")
s = pd.Series([99,98,56,45],index=["a","b","c","d"])
s1 = pd.Series([1,2,3,4])
print(s+e)
#print(s["Prashant"])
#print(s.iloc[0])
d = {"a":9,"b":10,"c":11,"d":12}#indexing(index value ) should be same
s3 = pd.Series(d)
s5 = pd.Series([1000,1000,1000,1000])
print(e+s3)
s4 = pd.Series(d,index=["a","d"])
print(s+s5)
print(s4)



s6 = pd.Series(42,index=["sagar","prashant"])
print(s6)
temp = [10.1,2.2,3.3,5.6,7.9,3,-3]
s7 = pd.Series(temp,index=["a","b","c","d","e","f","g"], name = "Temperature")
s7.plot()
plt.show()


s8 = e+s
s8.plot()
plt.show()

dd = {"A":[1,2,3],"B":[4,5,6]}
dtframe = pd.DataFrame(dd)
print(dtframe)
data = {
    "Series_A": pd.Series([10, 20, 30], index=["a", "b", "c"]),
    "Series_B": pd.Series([40, 50, 60], index=["a", "b", "c"]),
    "Series_C": pd.Series([70, 80, 90], index=["a", "b", "c"]),
}
dt = pd.DataFrame(data)
print(dt)
dt.plot()
plt.show()
print(dt[np.array([True,False,True])])
dt = {
    "weight": pd.Series([60, 83, 112], index=["alice", "bob", "charles"]),
    "birthyear": pd.Series([1989, 1969, 1999], index=["bob", "charles", "alice"], name="year"),
    "children": pd.Series([0, 3], index=["charles", "bob"]),
    "hobby": pd.Series(["biking", "dancing"], index=["alice", "bob"])
}


df = pd.DataFrame(dt)
print(df)

#access a column
print(df["birthyear"])

#Access multiple columns
print(df[["birthyear", "hobby"]])


#include column or row
d2 = pd.DataFrame(dt, columns = ["birthyear","weight","height"],index = ["bob","alice","eugene"])
print(d2)

#access a row
print(df.loc["charles"])
print(df.iloc[2])
#get slice of rows
print(df.iloc[1:3])
print(df[df["birthyear"] < 1990])
df["age"] = 2016 - df["birthyear"]
print(df)
df["over 30"] = df.pop("birthyear")
del df["children"]
print(df)


df.insert(2,"height",[123,456,789])
print(df)
#sorting
s = df.sort_index(ascending=False)
print(s)
print(df)
#do direct change in dataframe we can use inplace
df.sort_index(inplace=True,ascending=False)
print(df)
#df.sort_values(by="age",inplace=True)
#print(df)
df.plot()
plt.show()
df.plot(kind = "line",x="age",y = ["height","weight"])
plt.show()
df.to_csv("dt_csv.csv")
data = pd.read_csv("dt_csv.csv")
print(data.head())
print(data.tail(n=2))
print(data.info())
print(data.describe())

d = {"Sagar":pd.Series([12,15,16,44], index = ['a','b','c','d']) ,"Prashnat":pd.Series([56,18,78,56], index = ['a','b','c','d'])}
df = pd.DataFrame(d)
print(df)
print(df.head)'''
df = pd.read_csv("data.csv")
print(df.isnull().sum())
ndf = df.dropna()
print(ndf)
df.dropna()
print(ndf.isnull().sum())
null_row = df[df.isnull().any(axis=1)]
print("Row having null values")
print(null_row)
print(df[df["Calories"].isnull()])
mean_calorie = ndf["Calories"].mean()
print(mean_calorie)
df["Calories"].fillna(mean_calorie,inplace=True)
#print(df)
print(df.isnull().sum())
df.to_csv("new_data.csv")

