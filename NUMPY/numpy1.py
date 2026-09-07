#!/usr/bin/env python
# coding: utf-8

# NUMPY INDEXING AND SLICING EXAMPLES

# In[2]:


import numpy as np

# Create the array
a = np.array([[10, 20, 30], 
              [40, 50, 60]])

print("=" * 50)
print("NUMPY INDEXING AND SLICING EXAMPLES")
print("=" * 50)


# In[3]:


print("Original array:")
print(a)
print("Shape:", a.shape)


# In[4]:


# Access element at row index 1, column index 2
# Remember: indexing starts at 0!
element = a[1, 2]  # 60
print("Element at row 1, column 2:", element)


# In[5]:


# Select all rows (:) and column index 1
column = a[:, 1]  # [20, 50]
print("All rows, column 1:", column)


# In[6]:


# Select rows 0 to 1 (0:2) and columns 0 to 1 (0:2)
# Note: 0:2 means include 0 and 1, but exclude 2
subarray = a[0:2, 0:2]  # [[10, 20], [40, 50]]
print("Subarray (rows 0-1, cols 0-1):")
print(subarray)


# In[7]:


# Select last row (-1) and all columns (:)
last_row = a[-1, :]  # [40, 50, 60]
print("Last row:", last_row)


# In[8]:


empty_array = np.array(object = [])


# In[9]:


empty_array


# In[ ]:


type(empty_array) 


# In[11]:


empty_array.size


# In[12]:


my_array = np.array([1, 2, 3])
my_array


# In[13]:


type(my_array)


# In[14]:


my_array.dtype


# In[15]:


my_array.shape


# In[ ]:


# Create empty array (values are random/garbage)
empty_arr = np.empty((2, 3))
print("Empty array (2x3):")
print(empty_arr)
print("⚠️ Values are random - whatever was in memory!")
print()


# In[20]:


# Create empty array with specific data type
empty_int = np.empty((1, 2, 3), dtype=int)
print("Empty int array:")
print(empty_int)


# In[21]:


# 2. np.zeros() - initialized with zeros
zeros = np.zeros((2, 2))
print("2. np.zeros():")
print(zeros)
print("→ All values are 0\n")


# In[ ]:


# 3. np.ones() - initialized with ones
ones = np.ones((2, 2, 3))
print("3. np.ones():")
print(ones)
print("→ All values are 1\n")


# In[27]:


# 4. np.full() - filled with a specific value
full = np.full((4, 8), 7)
print("4. np.full():")
print(full)
print("→ All values are 7\n")


# In[28]:


# 3. np.ones() - Array of ones
print("3. np.ones() - All ones")
print("-" * 40)
ones = np.ones((2, 3))
print(f"np.ones((2,3)):\n{ones}")
print(f"Shape: {ones.shape}\n")


# In[29]:


# 4. np.full() - Fill with specific value
print("4. np.full() - Specific value")
print("-" * 40)
full = np.full((2, 3), 9)
print(f"np.full((2,3), 9):\n{full}")
print(f"Shape: {full.shape}\n")
print(f"Size: {full.size}\n")

# 5. np.random.random() - Random floats in [0.0, 1.0)
print("5. np.random.random() - Random floats")
print("-" * 40)
random_array = np.random.random((2, 3))
print(f"np.random.random((2,3)):\n{random_array}")
print(f"Shape: {random_array.shape}\n")
print(f"Size: {random_array.size}\n")

# 6. np.random.randint() - Random integers in a specified range
print("6. np.random.randint() - Random integers")
print("-" * 40)
randint_array = np.random.randint(1, 10, size=(2, 3))
print(f"np.random.randint(1, 10, size=(2,3)):\n{randint_array}")
print(f"Shape: {randint_array.shape}\n")
print(f"Size: {randint_array.size}\n")

# 7. np.random.randn() - Random samples from the standard normal distribution
print("7. np.random.randn() - Standard normal distribution")
print("-" * 40)
randn_array = np.random.randn(2, 3)
print(f"np.random.randn(2, 3):\n{randn_array}")
print(f"Shape: {randn_array.shape}\n")
print(f"Size: {randn_array.size}\n")


# In[30]:


# 8. np.random.choice() - Random samples from a given 1-D array
print("8. np.random.choice() - Random samples from a given 1-D array")
print("-" * 40)
choice_array = np.random.choice([1, 2, 3, 4, 5], size=(2, 3))
print(f"np.random.choice([1, 2, 3, 4, 5], size=(2, 3)):\n{choice_array}")
print(f"Shape: {choice_array.shape}\n")
print(f"Size: {choice_array.size}\n")


# In[31]:


# 7. np.linspace() - Evenly spaced values
print("7. np.linspace() - Evenly spaced")
print("-" * 40)
linspace = np.linspace(0, 1, 5)
print(f"np.linspace(0, 1, 5) → {linspace}")
print("→ 5 numbers between 0 and 1\n")


# In[32]:


# 8. np.eye() - Identity matrix
print("8. np.eye() - Identity matrix")
print("-" * 40)
eye = np.eye(3)
print(f"np.eye(3):\n{eye}")
print("→ 1s on diagonal, 0s elsewhere\n")


# In[33]:


my_array = np.array(['yes', 'no', 'maybe'])
my_array


# In[34]:


np.arange(start = 1, stop = 10)


# In[36]:


np.array(range(1, 10))


# In[38]:


np.array(range(1, 10, 2)) #np.arange(start = 1, stop = 10, step = 2)


# In[39]:


np.zeros(shape = 10)


# In[ ]:




