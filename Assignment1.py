#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
arr= np.array([1,2,3,4,5,6])
print(arr)


# In[3]:


import numpy as np

print(np.__version__)


# In[6]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
print(arr[0])
print(arr[1] + arr[3])


# In[7]:


import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])


# In[16]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr[1:5])
print(arr[4:])
print(arr[:3])
print(arr[-3:-1])
print(arr[1:5:2])


# In[21]:


import numpy as np 
arr=np.array([4,5,6,7,8])
x=arr.copy()
arr[0]=43
print(arr)


# In[22]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# In[23]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)


# In[24]:


import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)


# In[25]:


import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)


# In[26]:


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


# In[27]:


import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


# In[28]:


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)


# In[29]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


# In[30]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)


# In[ ]:




