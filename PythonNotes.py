#!/usr/bin/env python
# coding: utf-8

# # Revision

# In[1]:


print("Hello")


# In[2]:


#comment (simgle line comment)
'''asd
fg
asd
qw
e
eqwe (Multi line Comment)'''
# multi-line comment also by ctrl+/


# In[3]:


#variable (it is a container which holds some value)
#variable declaration asd=1, a_s=2, _a_s=3,aA=4, a1=5


# In[4]:


# [] - List in square Bracket
a = [1,"Anurag",22]
print(a)
print(type(a))
# () - Tuple in round bracket (parentheses)
b = (1,"Anuj",22)
print(b)
print(type(b))
# {} - Dictionary in curly bracket
c = {"name":"Anurag","age":22}
print(c)
print(type(c))


# # Keyword

# In[5]:


help()


# In[6]:


help(print)


# # Operators

# # Airthematic Operator

# In[7]:


# +,-,*,/,%,//


# In[8]:


a=52
b=47
c=a+b
print(c)


# In[9]:


print(4+9)


# In[10]:


print(9-8)


# In[11]:


print(8*9)


# In[12]:


print(81/9)


# In[13]:


print(99%9)
print(99%8)


# In[14]:


#Floor Division
print(7//2)


# In[15]:


print(7/2)


# In[16]:


#Exponent
print(2**4)
print(5**5)


# # Assignment Operator

# In[17]:


# +=, -=, *=, /=, %=, **=
a=5
print(a)
a+=9
print(a) #14
a-=4
print(a) #10
a*=2
print(a) #20
a/=4
print(a) #5
a%=3
print(a) #2
a**=3
print(a) #8


# # Comparison Operator

# In[18]:


#Comparison - Return TRUE or FALSE
# ==, !=, >, >=, <=


# In[19]:


a=5
b=6
c=10
print(c==a+b) #false
print(a>=c) #false
print(b>=a) #true
print(b>a) #true
print(a>b) #false
print(c<a+b) #true
print(c>=a+b) #false
print(a!=b) #true


# # Logical Operator

# In[20]:


#AND, OR, NOT


# In[21]:


a=10
b=20
c=30
d=40
print(a+b==c and c>d)
print(a+b==c and d>c)
print(a+b==c or c>d)
print(not(a+b==c or c>D))


# # Mutable and Immutable

# In[22]:


#Mutable
#Mutable object is one whose value may change in place.

#Immutable
#In immutable variables change of values will not happen in place. 
#Modifying in an immutable variables will rebuild the same variable.


# # Identity Operator

# In[23]:


#is, is not


# In[24]:


a=5
b=10
print(a==b)
print(a is b)
print(a is not b)


# # Membership Operator

# In[25]:


#in, not in


# In[26]:


a="python"
print('p' in a)
print('P' in a)
print('x' in a)
print('on' in a)
print('oN' in a)


# # Datatypes

# In[27]:


#Numbers:
#int, float, complex
a=5
print(a)
print(type(a))
b=2.5
print(b)
print(type(b))
c=2+5j
print(c)
print(type(c))
d=a+c
print(d)
print(type(d))


# In[28]:


#String 
#Denoted by " ",''' ''',' '
#Concatenation
#Indexing
#Slicing
#Methods
a="Anurag"
print(a)
s='''My name is
Anurag
Singh
Pundir'''
print(s)


# In[29]:


# \n is line break character and 
# \t is one tab-space between characters
print("H\nE\nL\nL\nO")
print("H\tE\tL\tL\tO")


# In[30]:


a="Hello"
b="World"
c=" "
d=a+b
print(d)
e=a+c+b
print(e)
print(a+'\t'+b)


# # Indexing

# In[31]:


#Indexing starts from 0, so the string hello would be:
#character: h e l l o
#index:     0 1 2 3 4

#You can use square brackets to grab single character
#Reverse Indexing: h e l l o:-5 -4 -3 -2 -1


# In[32]:


a="python"
print(a[4]) #o
print(a[3]) #h
print(a[-1]) #n
print(a[-6]) #p


# # Slicing

# # Syntax
# # [start:stop:step]
# # step is default 1
# # if no start is given  and step is +ve the start is 0
# # if no start is given and step is -ve then start is -1 

# In[33]:


alpha = 'abcdef'
alpha[0:3]


# In[34]:


dear = "Anurag"
dear[1:5]


# In[35]:


student = "Anurag Singh Pundir"
student[2:18:2]


# In[36]:


place = "Saharanpur"
place[1:5:-1]


# In[37]:


place = "Meerut Noida"
place[0::2]


# In[38]:


a="Hello India"
print(a[6:])
print(a[1:9:2])


# # If we dont give any stop and step is positive then the entire string is sliced from start to end in direction of left to right
# # If we dont give any stop and step is negative then the entire string is sliced from start to end in direction of right to left

# In[39]:


p="Hello"
print(p[::-1])
print(p[0::])
print(p[::])
print(p[:])


# # Methods

# In[40]:


dir(str)


# In[41]:


dir(int)


# In[42]:


a="singh is king"
print(a)
c=a.upper()
ca=a.capitalize()
t=a.title()
print(c)
print(ca)
print(t)


# In[43]:


a=" I am DevOps Engineer "
print(a.center(50,"*"))


# In[44]:


# There are various check methods which apply to a string to check for some condition
a="python123"
print(a.islower())
print(a.isupper())
print(a.isalpha())
print(a.isalnum())
print(a.isdigit())
print(a.startswith('py'))
print(a.endswith('n'))


# In[45]:


b="DevilMayCry"
print(b)
c=b[::-1]
print(c)
r=b.replace('y','$',2)
print(r)


# In[46]:


help(str.strip)


# In[47]:


a="                 Far  Cry "
print(a,type(a))
b=a.strip()
print(b)


# In[48]:


help(str.find)


# # List

# # Denoted by[] and items are separated using a 
# # Concatenation
# # Indexing, Slicing
# # Methods
# # a=[]-----------> Empty List

# In[49]:


a=[]
print(a,type(a),len(a))


# In[87]:


#Homogenous Data ------> same type
a=[10,20,30,40]
print("Homogenous Data",a)
#Heterogenous Data ------> multiple types
b=["Hello",7,8,6,"Far","Cry",[6.0,"New Dawn",5.0,"Primal",4,3,2,1]]
print("Heterogenous Data",b)


# In[89]:


#Concatenation
a=[1,2,3]
b=[4,5,6]
print(a,b,id(a))
c=a+b
print(c)


# # Indexing and Slicing

# In[90]:


#It works the same way it worked on string


# In[99]:


a=[[10,20],["Hello","Python"],["Hello"]]
print(a,"Length:",len(a))
print(a[0])
print(type(a))


# In[98]:


a=[]
print(type(a))
b=()
print(type(b))
a=[1,2,3]
print(a,type(a))


# In[102]:


help(list.pop)


# In[110]:


a=[10,20,30]
print(a,type(a))
b=a.append(40)
print(a,b)
a.append([1,2,3])
print(a)
a.insert(1,40) #insert method add item to the index position mentioned
print(a)
a.remove(40)#remove method deletes the values passed as an argument
print(a)
a.pop(1)
print(a)
a.pop()
print(a)


# In[53]:


a=5,4
print(a)
print(type(a))
b=1,"one"
print(b)
print(type(b))
c=[1,2],[3,4]
print(c)
print(type(c))


# # Conditional_Statement

# In[ ]:




