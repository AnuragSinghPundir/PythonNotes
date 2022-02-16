#!/usr/bin/env python
# coding: utf-8

# # Conditional_Statement

# # Keywords:
# # 1. if
# # 2. else
# # 3. elif--->else if(to check multiple condition)
# 
# # BLocks:
# # 1. if block
# # 2. if else block
# # 3. nested if else block
# # 4. if elif block
# # 5. if elif else block

# # Syntax
# # if condition:
#     # body of if
# # elif condition:
#     # body of elif
# # else condition:
#     # body of else

# In[3]:


#if block
a=int(input("Enter a number: "))
if a%2==0:
    print("You have entered an Even Number")
else:
    print("You have entered an Odd Number")
print("Further Code:----")
    


# In[8]:


#Nested if else
a=int(input("Enter a number: "))
if a%2==0:
    if a%3==0:
        print(a,"is divisible by both 2 and 3.")
    else:
        print(a,"is divisible by 2 only.")
else:
    if a%3==0:
        print(a,"is divisible by 3 only.")
    else:
        print(a,"is divisible by neither 2 nor 3.")


# In[ ]:




