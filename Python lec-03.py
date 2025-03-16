#Logical operators- and,or,not

a=5
print('a>3 and a<5:',a>3 and a<5)
print('a>3 or a<5:',a>3 or a<5)
print('not(a>3 and a<5):',not(a>3 and a<5))

#Conditional Statements
#if-else loop

a=int(input())
if(a>=18):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")


a=int(input())
b=int(input())
if(a>b):
    print(" a is greater than b")
elif(a==b):
    print("a is equal to b")
else:
    print("b is greater than a")

#while loop

i=0
while i<5:
    print(i)
    i+=1
print(i)

#for loop

for x in "banana":
    print(x)

#break and continue
#try except

try:
    x=10/0
except ZeroDivisionError:
    print("cannot divide by zero")


try:
    print(x)
except:
    print("something is wrong")

#Function

a=int(input("enter a: "))
b=int(input("enter b: "))
def add(c,d):
    print("addition:",c+d)
add(a,b)


def add(a,b):
    return a+b
c=3
d=4
result=add(c,d)
print(result)

#Modules

import module as m
a=m.student["name"]
print(a)
m.greeting(" John")
//from keyword































