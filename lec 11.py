import pandas as pd

df=pd.read_csv("data.csv")
print(df)
print("----------")
ndf=df.dropna()
print(ndf.isnull().sum())

print(df.isnull().sum())
print("----------")

df.dropna(inplace=True)
print(df.isnull().sum())
print("----------")

df=pd.read_csv("data.csv")
df.fillna(130,inplace=True)
print(df.isnull().sum())

print("mean:",df.mean(axis=1))
print("median:",df.median(axis=1))
print("mode:",df.mode(axis=1))

x=df["Calories"].mean()
df["Calories"]=df["Calories"].fillna(x)

#2 - Mean()

df=pd.read_csv("Data.csv")
null_rows=df[df.isnull().any(axis=1)]
print(null_rows)
x=df["Pulse"].mean()
df["Pulse"]=df["Pulse"].fillna(x)
print(df.isnull().sum())

#3- Median(), Mode()

df=pd.read_csv("Data.csv")
x=df["Calories"].mode()[0]
print(x)
df["Calories"]=df["Calories"].fillna(x)
print(df[df["Calories"]==x])
y=df["Pulse"].median()
print(y)
df["Pulse"]=df["Pulse"].fillna(y)
print(df["Pulse"])
print(df.isnull().sum())

#practice question
df=pd.read_csv("dataset.csv")
print(df.describe())
print(df.head(n=2))
print(df.isnull().sum())
x=df["Calories"].mean()
df["Calories"]=df["Calories"].fillna(x)
print(df.isnull().sum())
y=df["Pulse"].median()
df["Pulse"]=df["Pulse"].fillna(y)
print(df.isnull().sum())
z=df["Maxpulse"].mean()
df["Maxpulse"]=df["Maxpulse"].fillna(z)
print(df.isnull().sum())
df.to_csv("final.csv")

















