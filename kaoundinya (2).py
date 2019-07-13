#!/usr/bin/env python
# coding: utf-8

# # python
# 
# 

# In[ ]:





# 
# 
# http//www.google.com 

# In[ ]:


print("hello,gitam","|||",end=" ")


# In[ ]:


print("hello world " )


# In[5]:


a1=int(input("enter the a"))
a2=int(input("enter the b"))
a3=int(input("enter the c"))
if a1>a2 and a1>a3:
    
    print(a1,"is largest")
elif a2>a1 and a2>a3:
    print(a2,"is largest")
else:
    print(a3,"is largest")        


# In[ ]:


#sum of even digits usuing functions
def addevendigits(n):
        sum=0
        while n!=0:
             r=n%10
        if r%2==0:
            sum=sum+r
        n=n//10
        print(sum)
n=int(input("enter a number"))
addevendigits(n)


# In[ ]:


#to recerse a number
def reverse(n):
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//1
    return(s)
n=int(input("enter a number"))
reverse(n)


# In[7]:


#given number is palindrome or not
def pallindrome(n):
    s=0
    k=n
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if k==s:
        print("pallindrome")
    else:
        return "not a pallindrome"
n=int(input("enter a number"))
pallindrome(n)


# In[1]:


#given number is aprime or not
def isprime(n):
    flag = true
    for i in range(2,n//2+1):
        if n% i == 0:
            flag = false
            return flag
        return flag
    isprime(11)


# In[7]:


# function to find prime number count from 1 to N
# n= --4(2,3,4,7)
def primecount(N):
    cnt = 0
    for a in range(2,N+1):
        k=0
        for i in range(2,a//2+1):
            if a%i == 0:
                k=k+1
        if(k<=0):
            cnt=cnt+1
    return cnt
primecount(6)
        
        


# In[1]:


# Function to print "Python" if the count of
# Upper and lower case is same
# Print "Programming" if not same
# ex: PyThOn ---3 P T O (upper case)
#              3 y h n (lower case)
#PytHon --P H (2)
#       --y t o n(4) -Programming


def findCount(str):
   cntUpper =0
   cntLower =0
   for x in range(len(str)):
       if ord(str[x]) >=65 and ord(str[x])<=90:
           cntUpper=cntUpper+1
       elif ord(str[x]) >=97 and ord(str[x])<=122:
           cntLower=cntLower+1
   if cntUpper == cntLower:
       return "SameCount"
   else:
       return "Programming"
   return
print(findCount('PyThOn'))  #SameCount
print(findCount('PYTHon'))  #Programming


# In[13]:


#function to return the sum of digits given string
#example:
#input:appli1cat8ion89
#output:26(1+8+8+9)
def sumofdigits(str):
    sum = 0
    for x in range(len(str)):
        if ord(str[x]) >=48 and ord(str[x]) <=57:
             if(ord(str[x]-48)) % 2 == 0:
            sum = sum + (ord(str[x])-48) 
sumofdigits('appli1cat8ion89')


# In[ ]:


#function to return the sum of digits given string
#example:
#input:appli1cat8ion89
#output:16(8+8) 
def sumofevendigits(str):
    sum = 0
    for x in range(len(str)):
        if ord(str[x]) >=48 and ord(str[x]) <=57:
             if(ord(str[x]-48)) % 2 == 0:
            sum = sum + (ord(str[x])-48) 
sumofdigits('appli1cat8ion89')


# ### Python data structure
# #### Lists
# - it's one of common data structure supports by python,the list items are seperated by comma operators are enclosed in square brackets
# 

# In[6]:


lst=[1,8,16,9,2] 
print(lst)# Access the entire list
print(lst[0])#Access the first item list
print(lst[1])#Access the second item list
print(lst[-1])#Access the last itme list
print(lst[-2])
print(lst[1:])
print(lst[1:4])


# In[9]:


#To delete specific item in list
x=[1,2,567,876]
print(x)
del x[1]
print(x)


# In[12]:


#Basic list operations
lst1 = [1,9,6,18,2]
print(len(lst1))# len of the list
print(lst1 * 2) #repetation
print(len(lst1))
print(9 in lst1)
print(15 in lst1)
for x in range(len(lst1)):
    print(lst1[x],end=' ')


# In[16]:


lst1
lst1.append(24) # Adding a new element at the end of the list
lst1
lst1.insert(2,56)# Adding an element at partation index
lst1
lst1.count(18)# Return the value how many times the object repeated
lst1.index(56)
lst1.sort() # It's sort the list in ascending order
lst1
lst1.pop() # remove the last element from the list
lst1
lst.pop(1) # Remove an element from a particular index
lst2 =[123,23,45]
lst1.extend(lst2)# Merge the list2 into list1
lst1


# In[18]:


#function to find the second large item from tne list 
#input : [1,19,6,2,18,3]
# output :18
def secondlarge(li):
    li.sort()
    return li[-2]
li = [1,19,6,2,8,18,3]
secondlarge(li)    


# # DICTIONARIES
# ### It works on the concept of set unique data
# 

# In[2]:


d1 = {"name":"Gitam","Email":"gitam@gmail.com","address":"hyderabad"}
print(d1)


# In[4]:


d1['emailid'] = "itam-python@gmail.com"


# # assingment programe
# 

# In[8]:


def reverseFibonacci(n): 
   
    x = [0] * n  
  
    # assigning first and second elements 
    x[0] = 0 
    x[1] = 1 
  
    for i in range(2, n):   
  
        # storing sum in the 
        # preceding location 
        x[i] = x[i - 2] + x[i - 1]  
       
  
    for i in range(n - 1, -1 , -1):   
  
        # printing array in 
        # reverse order 
        print(x[i],end=" ")  
       
   
  
# Driver function 
n = 12 
reverseFibonacci(n)


# In[9]:


#*** Function to count the occurances of a character in a string
def repeat(x,target):
    c=0
    for i in x:
        if i==target:
            c+=1
    return c
# (OR)
#def repeat1(x,target):
#    return x.count(target)
a=str(input("enter a string-"))
b=str(input("enter target element-"))
repeat(n,m) 


# In[1]:


#8. Your Program has to read one string as well as one character and you need to remove the all the occurance of the character.

#HebeonTech,e -- HbonTch
def delete(n,target):
    c=0
    for i in range(len(n)):
        if n[i]==target:
            c+=1
    print(n.replace(target,"",c))
n=str(input("enter a string"))
target=str(input("enter a char"))
delete(n,target)


# In[2]:


# 9. Your Program need to accept two strings and generate the output in merging of both strings.
def comb(a,b):
    c=a+b
    return c 
a=str(input("enter a string "))
b=str(input("enter a string "))
comb(a,b)


# In[4]:


# 10. Series Generations:-  1, 3, 9, 27, 81, ...
def square(n):
    for i in range(n):
        print(3**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[6]:


# 11. Series Generations:-  1, 2, 4, 8, 16, 32, 64, 128, 256, ...
def square(n):
    for i in range(n):
        print(2**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[7]:


# 12. Series Generations:-  1 3 4 8 15 27 50 92 169 311
def series(n):
    a=1
    b=3
    c=a+b
    print(a,b,c,end=" ")
    for i in range (4,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
        print(d,end=" ")
    return
n=int(input("enter a number"))
series(n)


# In[10]:


# 14. Series Generations:-  1! + 2! + 3! + 4! + 5! + ... + n!
def fact(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return f   
def series(m):
    s=0
    for x in range (1,n+1):
        s=s+fact(x)
    return s
n=int(input("enter n"))
series(n)


# In[11]:


# 6
def findNthTerm(n): 
   if n % 2 == 0: 
       n //= 2
       print(3 ** (n - 1)) 
   else: 
       n = (n // 2) + 1
       print(2 ** (n - 1)) 
if __name__=='__main__': 
   N = 3
   findNthTerm(N) 
   N = 21
   findNthTerm(N) 


# In[12]:


# 13. Series Generations:-  2 15 41 80 132 197 275 366 470 587
def series(n):
    a=2
    print(a,end=" ")
    for i in range (1,n+1):
        b=a+(13*i)
        print(b,end=" ")
        a=b
    return
n=int(input("enter a number"))
series(n)


# In[ ]:


def Q2(n):
    a=[]
    s=0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j:
                if a[i]==a[j]:
                    c+=1
        if c==0:
            s=s+a[i]
    return s
Q2(int(input("no of values")))


# In[ ]:


def Q3(a,b):
    if len(a)<=len(b):
        n=len(a)
        k=len(b)
    else:
        n=len(b)
        k=len(a)
    for i in range(n):
        print(a[i],b[i])
    for j in range(n,k):
        if(len(a)<=len(b)):
            print(b[j],'*')
        else:
            print(a[j],'*')
    return
x=str(input("enter str:"))
x=x.split()
Q3(x[0],x[1])


# In[ ]:


def Q4(a,b):
    if len(a)>=len(b):
        print(a.upper())
    else:
        print(b.upper())
    return
x=str(input("enter str:"))
x=x.split()
Q4(x[0],x[1])


# In[ ]:


def Q5_1(a):
    a=a.split()
    for i in range (len(a)):
        if a[i].istitle()==True:
            print(a[i].upper(),end= " ")
    return
x=str(input("enter str:"))
Q5_1(x)


# In[ ]:


def Q7(n):
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        for j in range(n[i]):
            print("*",end="")
        print("")
    return
x=input("enter num")
Q7(list(x))


# In[ ]:


# 1. The program must accept an integer N as the input. 
# The program must print the fibonacci series in the reverse order as the output.


def reversefib(n): 
    a = [0]*n 
    a[0] = 0 
    a[1] = 1 
    for i in range(2, n):
        a[i] = a[i - 2] + a[i - 1]  
    for i in range(n - 1, -1 , -1):   
        print(a[i],end=" ") 
    return 
reversefib(5)

reversefib(12)


# In[1]:


import os
dirPath='git/'
for f_name in os.listdir(dirPath):
   if f_name.endswith('ipynb'):
       print(f_name)


# In[ ]:


li=os.scandir('git/')
for i in li:
   print(i)


# In[ ]:


from pathlib import Path
li=Path('git/')
for i in li.iterdir():
   print(i.name)


# In[2]:


import os 
dirPath = "git/"
for i in os.listdir(dirPath): # All files and folders
   if os.path.isfile(os.path.join(dirPath,i)):
       print(i)


# In[3]:


dirPath='git/'
with os.scandir(dirPath)as f:
   for i in f:
       if i.is_file():
           print(i.name)


# #   Listing SubDirectories

# In[4]:


In [34]:
dirPath='git/'
for i in os.listdir(dirPath):
if os.path.isdir(os.path.join(dirPath,i)):
print(i)


# In[5]:


from pathlib import Path
dirPath=Path('git/')
for i in dirPath.iterdir():
   if i.is_dir():
       print(i.name)


#  # Creating a Single Directory

# In[6]:


In [61]:
import os
os.mkdir('single directory')


# In[8]:


import pathlib
p=pathlib.Path('TestFolder')
p.mkdir()


# # Creating Multiple Directory

# In[9]:


In [60]:
import os
os.makedirs('2019/july/11/Thursday')


# In[11]:


ls


# In[10]:


import os
dirPath='git/'
for f_name in os.listdir(dirPath):
   if f_name.endswith('ipynb'):
       print(f_name)


# In[12]:


import os
dirPath='git/'
for f_name in os.listdir(dirPath):
   if f_name.startswith('ipynb'):
       print(f_name)


# In[13]:


import os
data_file="single directory"# give the entire path
os.rmdir(data_file)


# In[14]:


import shutil # delete the tree of structure of folder
data_dir='2019'
shutil.rmtree(data_dir)


# In[15]:


ls


# # Regular Expression
# - Pattern matching
# - pattern(re) package
# - [0-9]-->any digit matching
#   > Two digit number (^[0-9]{2}$)

# In[3]:


#Function to the test two digit number matching
import re
def twodigitmatching(n):
    pattern = '^[0-9]{2}$'
    n=str(n)
    if re.match(pattern,n):
        return True
    return False
print(twodigitmatching(12)) #true
print(twodigitmatching(123))#false


# In[9]:


# Function to test roll number motching
import re
def match(n):
    pattern='^[1][5][2][1][A][0-9]{4}$'
    n=str(n)
    if re.match(pattern,n):
        return True
    return False
n=str(input("enter roll number "))
match(n)


# In[6]:


# Function to test password motching
import re
def match(n):
    pattern='^[A-za-z0-9@#!]{6,15}$'
    n=str(n)
    if re.match(pattern,n):
        return True
    return False
n=str(input("enter a number "))
match(n)


# In[1]:


#Hexagon with multi colour
from turtle import *
colors = ['blue','green','yellow','orange','purple','red']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(50)


# In[2]:


# undo() function will undo the turtle last action
from turtle import *
pencolor('black')
for i in range (10):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
pencolor('red')
for i in range(90):
    undo()


# In[ ]:




