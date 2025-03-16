#LIST

a=[1,'banana','python',2]
print(type(a))
print(a)
print(a[3:])
print(a[0:2])
print(a+a)
print(a*3)

#TUPLES

tup=(1,"python",2)
print(type(tup))
print(tup)
print(tup[1:])
print(tup+tup)
print(tup*3)
print(tup[-1])


a=(2)
print(type(a))
b=(2,)
print(type(b))

#SET

s={"apple","banana",True,1,False,0,2} #True represent  1 and false reresent 0
print(s)
s.add(5)
print(s)
s.remove(5)
print(s)

#control struc, modules,functions revise them
#membership (in and not in)

s={"apple","banana"}
print("banana" in s)
print("banana" not in s)

#dictionary

d={"subject" :"python",2:"data"}
print(d)


print(int(True))
print(bool(3))
print(bool(0))

#operators:-

"ARITHEMATIC"
a=int(input())
b=int(input())
add=a+b
sub=a-b
mul=a*b
div=a/b
rem=a%b
floor=a//b
exp=a**b
print(add,"\n",sub,"\n",mul,"\n",div,"\n",rem,"\n",floor,"\n",exp)


"COMPARISON"
a=int(input())
b=int(input())
print(a!=b)
print(a==b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
#assignment operators
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)








