#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a = np.arange(1, 10)
print(a)
x = range(1, 10)
print(x)    # x is an iterator
print(list(x))

# further arange examples:
x = np.arange(10.4)
print(x)
x = np.arange(0.5, 10.4, 0.8)
print(x)


# In[3]:


import numpy as np
# 50 values between 1 and 10:
print("50 values between 1 to 10",np.linspace(1, 10))
# 7 values between 1 and 10:
print("7 values between 1 to 10 ",np.linspace(1, 10, 7))
# excluding the endpoint:
print("excluding end points",np.linspace(1, 10, 7, endpoint=False))


# In[4]:


import numpy as np
x = np.array(42)
print("x: ", x)
print("The type of x: ", type(x))
print("The dimension of x:", np.ndim(x))


# In[5]:


import numpy as np
x = np.array(42)
print("x: ", x)
print("The type of x: ", type(x))
print("The dimension of x:", np.ndim(x))


# In[6]:


import numpy as np
x = np.array(42)
print("x: ", x)
print("The type of x: ", type(x))
print("The dimension of x:", np.ndim(x))


# In[7]:


B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])
print(B)
print(B.ndim)


# In[8]:


x = np.array([ [67, 63, 87],
               [77, 69, 59],
               [85, 87, 99],
               [79, 72, 71],
               [63, 89, 93],
               [68, 92, 78]])
print(np.shape(x))


# In[9]:


x.shape=(3, 6)
print(x)


# In[10]:


F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
# print the first element of F
print(F[0])
# print the last element of F
print(F[-1])


# In[11]:


A = np.array([ [3.4, 8.7, 9.9], 
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])

print(A[1][0])


# In[12]:


tmp = A[1]
print(tmp)
print(tmp[0])


# In[13]:


S = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(S[2:5])
print(S[:4])
print(S[6:])
print(S[:])


# In[14]:


A = np.array([
[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45],
[51, 52, 53, 54, 55]])

print(A[:3, 2:])
print(A[3:, :])
print(A[:, 4:])


# In[15]:


A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
S = A[2:6]
S[0] = 22
S[1] = 23
print(A)


# In[16]:


np.may_share_memory(A, S)


# In[17]:


A = np.arange(12)
B = A.reshape(3, 4)
A[0] = 42
print(B)


# In[18]:


import numpy as np
lst = [2,3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
v = np.array(lst)
v = v + 2
print(v)
print(v * 2.2)
print(v - 1.38)


# In[19]:


import numpy as np
A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = np.ones((3,3))
print("Adding to arrays: ")
print(A + B)
print("\nMultiplying two arrays: ")
print(A * (B + 1))


# In[20]:


import numpy as np
A = np.array([ [1, 2, 3], [2, 2, 2], [3, 3, 3] ])
B = np.array([ [3, 2, 1], [1, 2, 3], [-1, -2, -3] ])
R = A * B
print(R)


# In[21]:


import numpy as np
A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = np.array([ [11, 102, 13], [201, 22, 203], [31, 32, 303] ])
A == B


# In[22]:


print(np.array_equal(A, B))
print(np.array_equal(A, A))


# In[23]:


a = np.array([ [True, True], [False, False]])
b = np.array([ [True, False], [True, False]])
print(np.logical_or(a, b))
print(np.logical_and(a, b))


# In[24]:


import numpy as np
A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = np.array([1, 2, 3])
print("Multiplication with broadcasting: ")
print(A * B)
print("... and now addition with broadcasting: ")
print(A + B)


# In[25]:


B = np.array([[1, 2, 3],] * 3)
print(B)


# In[26]:


np.array([[1, 2, 3],] * 3).transpose()


# In[27]:


B = np.array([1, 2, 3])
B[:,np.newaxis]


# In[28]:


import numpy as np
A = np.array([[[ 0,  1],
               [ 2,  3],
               [ 4,  5],
               [ 6,  7]],
              [[ 8,  9],
               [10, 11],
 [12, 13],
               [14, 15]],
              [[16, 17],
               [18, 19],
               [20, 21],
               [22, 23]]])
Flattened_X = A.flatten()
print(Flattened_X)
print(A.flatten(order="C"))
print(A.flatten(order="F"))
print(A.flatten(order="A"))


# In[29]:


X = np.array(range(24))
Y = X.reshape((3,4,2))
Y


# In[30]:


import random
outcome = random.randint(1,6)
print(outcome)


# In[31]:


import random
outcome = random.randint(1,6)
print(outcome)


# In[32]:


import numpy as np
print(np.random.randint(1, 7))
print(np.random.randint(1, 7, size=1))
print(np.random.randint(1, 7, size=10))
print(np.random.randint(1, 7, size=(5, 4)))


# In[33]:


from random import choice
possible_destinations = ["Berlin", "Hamburg", "Munich", 
                         "Amsterdam", "London", "Paris", 
                         "Zurich", "Heidelberg", "Strasbourg", 
                         "Augsburg", "Milan", "Rome"]

print(choice(possible_destinations))


# In[34]:


import numpy as np
x = np.random.random_sample((3, 4))
print(x)


# In[35]:


B = np.array([[42,56,89,65],
              [99,88,42,12],
              [55,42,17,18]])

print(B>=42)


# In[36]:


C = np.array([123,188,190,99,77,88,100])
A = np.array([4,7,2,8,6,9,5])
R = C[A<=5]
print(R)


# In[37]:


import numpy as np
A = np.array([3,4,6,10,24,89,45,43,46,99,100])
div3 = A[A%3!=0]
print("Elements of A not divisible by 3:")
print(div3)
div5 = A[A%5==0]
print("Elements of A divisible by 5:")
print(div5)
print("Elements of A, which are divisible by 3 and 5:")
print(A[(A%3==0) & (A%5==0)])
print("------------------")
A[A%3==0] = 42
print("""New values of A after setting the elements of A, 
which are divisible by 3, to 42:""")
print(A)


# In[ ]:





# In[ ]:




