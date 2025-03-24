import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
a=np.arange(24).reshape(2,3,4)
print(a.sum(axis=0))
'''

b=pd.Series([18,20,16],index=["Ankit","Dipesh","Daksh"])
print(b)
print(b["Ankit"]) #By specifying label
print(b.loc["Dipesh"]) #Use loc when accessing by label
print(b.iloc[1]) #Use iloc when accessing by integer location1

c=pd.Series([15,46,78])
d=pd.Series([11,23,45])
print("add",c+d) #addition of series

weights={"Ankit":60,"Dipesh":81,"Daksh":68}
a=pd.Series(weights)
print("add list:",b+a) #addition between list and dictionary

s1=pd.Series(weights,index=["Daksh","Ankit"])
print(s1)

s2=pd.Series([1000,1000,1000])
print(b+s2)

s3=pd.Series(5,["v","s","f"])
print(s3)

s4=pd.Series([83,68],index=["bob","alice"],name="weights")
print(s4)

'''
import matplotlib.pyplot as plt
temp=[4.4,2.1,3.1,4.4,3.6,4.7,6.9,9.9,5.4,25.0]

s5=pd.Series(temp,name="Temperature",index=["a","b","c","d","e","f","g","h","i","j"])
s5.plot()
plt.show()
'''
'''
#DataFrame
import matplotlib.pyplot as plt
df={"a":[1,2,3],"b":[11,22,33]}
dd=pd.DataFrame(df)
dd.plot()
plt.show()
print(dd)
'''
#DataFrame
people={
    "weight": pd.Series([68,83,112],index=["alice","bob","charles"]),
    "birthyear": pd.Series([1985,1984,1992],index=["bob","alice","charles"], name="year"),
    "children": pd.Series([0,3],index=["charles","bob"]),
    "hobby": pd.Series(["Biking","Dancing"], index=["alice","bob"])
    }
#print(people)
dframe=pd.DataFrame(people)
print(dframe)
#dframe.plot()
#plt.show()
print(dframe[np.array([True,False,True])])
print(dframe["weight"]) #access a column
print("--------------")
print(dframe[["birthyear","hobby"]])
print("--------------")
#creating datfrme - include columns and /or rows and guarantee order

d2= pd.DataFrame(people,columns=["Birthyear","weight","height"],index=["bob","alice","eugence"])
print(d2)
print("--------------")
#accessing a row
print(dframe.loc["charles"])
print("-------------")
print(dframe.iloc[2])
print("--------------")
print(dframe.iloc[1:3])
print("--------------")
#pass a boolean expression
print(dframe[dframe["birthyear"]<1990])
print("--------------")
#Add a new column "age"
dframe["age"]=2025-dframe["birthyear"]
print(dframe)
print("--------------")
#add another columnn "over 30"
dframe["Over 30"]=dframe["age"]>30
print(dframe)
print("--------------")
#remove "birthyear and "children" columns
birthyears=dframe.pop("birthyear")
del dframe["children"]
print(dframe)
print("--------------")
dframe["pets"]=pd.Series({"bob":0,"charles":5,"eugiene":1})
print(dframe)
print("--------------")
#add a new  column using insert method after an existing column
dframe.insert(2,"height",[123,134,178])
print(dframe)
print("--------------")
s=dframe.sort_index(ascending=False)
print(s)
print(dframe) #original dataframe is not changed
print("--------------")
#To change sorting in original dataframe
dframe.sort_index(inplace=True,ascending=False)
print(dframe)
print("--------------")
#sorting by  value
dframe.sort_values(by="age",inplace=True)
print(dframe)
print("--------------")
#plotting
#dframe.plot()
dframe.plot(kind="bar",x="age",y=["height","weight"])
plt.show()
print("--------------")








