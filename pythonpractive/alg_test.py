
# coding: utf-8

# In[1]:


from sort import Sort
from insert_sort import InsertSort
from merge_sort import MergeSort
from quick_sort import QuickSort


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import random
import sys


# ## Generate Data and Sort

# In[24]:


isort = InsertSort([])
msort = MergeSort([])
qsort = QuickSort([])

i_runtime = []
m_runtime = []
q_runtime = []

i_jmptime = []
m_jmptime = []
q_jmptime = []

i_cmprtime = []
m_cmprtime = []
q_cmprtime = []


# In[25]:


for i in range(1, 10):
    isort.list = np.random.randint(i*1000, size = i*1000)
    msort.list = np.random.randint(i*1000, size = i*1000)
    qsort.list = np.random.randint(i*1000, size = i*1000)
    
    isort.time(isort.insert_sort)
    msort.time(msort.merge_sort)
    qsort.time(qsort.quick_sort)
    
    i_runtime.append(isort.run_time)
    m_runtime.append(msort.run_time)
    q_runtime.append(qsort.run_time)
    
    i_jmptime.append(isort.jump_time)
    m_jmptime.append(msort.jump_time)
    q_jmptime.append(qsort.jump_time)
    
    i_cmprtime.append(isort.compare_time)
    m_cmprtime.append(msort.compare_time)
    q_cmprtime.append(qsort.compare_time)


# In[35]:


i_runtime


# ## Plot Running Time

# In[36]:


# plot running time

r = range(9)
plt.plot(r, i_runtime, c="r", label="insert_sort")
plt.plot(r, m_runtime, c="b",  label="merge_sort")
plt.plot(r, q_runtime, c="g",  label="quick_sort")    

plt.legend()
plt.xlabel("NUMBER/k")
plt.ylabel("TIME")
plt.show()


# In[37]:


plt.plot(r, m_runtime, c="b",  label="merge_sort")
plt.plot(r, q_runtime, c="g",  label="quick_sort")

plt.legend()
plt.xlabel("NUMBER/k")
plt.ylabel("TIME")
plt.show()


# ## Plot Jump Time

# In[38]:


i_jmptime


# In[39]:



r = range(9)
plt.plot(r, i_jmptime, c="r", label="insert_sort")
plt.plot(r, m_jmptime, c="b",  label="merge_sort")
plt.plot(r, q_jmptime, c="g",  label="quick_sort")    

plt.legend()
plt.xlabel("NUMBER/k")
plt.ylabel("TIME")
plt.show()


# In[40]:


plt.plot(r, m_jmptime, c="b",  label="merge_sort")
plt.plot(r, q_jmptime, c="g",  label="quick_sort")    

plt.legend()
plt.xlabel("NUMBER/k")
plt.ylabel("TIME")
plt.show()


# ## Plot Compare Time

# In[43]:


r = range(9)
plt.plot(r, i_cmprtime, c="r", label="insert_sort")
plt.plot(r, m_cmprtime, c="b",  label="merge_sort")
plt.plot(r, q_cmprtime, c="g",  label="quick_sort")    

plt.legend()
plt.xlabel("NUMBER/k")
plt.ylabel("TIME")
plt.show()


# In[44]:


plt.plot(r, m_cmprtime, c="b",  label="merge_sort")
plt.plot(r, q_cmprtime, c="g",  label="quick_sort")    

plt.legend()
plt.xlabel("NUMBER/k")
plt.ylabel("TIME")
plt.show()


# ## Worst Condition

# In[54]:


ascend = range(1000)
descend = [x for x in ascend[::-1]]


# In[64]:


iw_runtime = []
mw_runtime = []
qw_runtime = []

iw_jmptime = []
mw_jmptime = []
qw_jmptime = []

iw_cmprtime = []
mw_cmprtime = []
qw_cmprtime = []


# ### ascend order

# In[65]:


sys.setrecursionlimit(3000)

isort.list = [x for x in ascend[:]]
msort.list = [x for x in ascend[:]]
qsort.list = [x for x in ascend[:]]

isort.time(isort.insert_sort)
msort.time(msort.merge_sort)
qsort.time(qsort.quick_sort)

iw_runtime.append(isort.run_time)
mw_runtime.append(msort.run_time)
qw_runtime.append(qsort.run_time)

iw_jmptime.append(isort.jump_time)
mw_jmptime.append(msort.jump_time)
qw_jmptime.append(qsort.jump_time)

iw_cmprtime.append(isort.compare_time)
mw_cmprtime.append(msort.compare_time)
qw_cmprtime.append(qsort.compare_time)


# ### descend order

# In[66]:


sys.setrecursionlimit(3000)

isort.list = [x for x in ascend[::-1]]
msort.list = [x for x in ascend[::-1]]
qsort.list = [x for x in ascend[::-1]]

isort.time(isort.insert_sort)
msort.time(msort.merge_sort)
qsort.time(qsort.quick_sort)

iw_runtime.append(isort.run_time)
mw_runtime.append(msort.run_time)
qw_runtime.append(qsort.run_time)

iw_jmptime.append(isort.jump_time)
mw_jmptime.append(msort.jump_time)
qw_jmptime.append(qsort.jump_time)

iw_cmprtime.append(isort.compare_time)
mw_cmprtime.append(msort.compare_time)
qw_cmprtime.append(qsort.compare_time)


# ### random order

# In[67]:


iw_runtime.append(i_runtime[0])
mw_runtime.append(m_runtime[0])
qw_runtime.append(q_runtime[0])

iw_jmptime.append(i_jmptime[0])
mw_jmptime.append(m_jmptime[0])
qw_jmptime.append(q_jmptime[0])

iw_cmprtime.append(i_cmprtime[0])
mw_cmprtime.append(m_cmprtime[0])
qw_cmprtime.append(q_cmprtime[0])


# In[68]:


iw_runtime


# ## Plot runtime

# In[70]:


label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(iw_runtime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()


# In[76]:


label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(mw_runtime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()


# In[75]:


label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(qw_runtime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()


# ## plot jump time

# In[83]:


label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(iw_jmptime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()


# In[78]:


label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(mw_jmptime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()


# In[79]:


label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(qw_jmptime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()


# ## plot compare time

# In[80]:


label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(iw_cmprtime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()


# In[81]:


label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(mw_cmprtime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()


# In[82]:



label_list = ["ascend", "descend", "random"]
color = ["red", "green", "blue"]
explode = [0.01, 0.01, 0.01]

plt.pie(qw_cmprtime, explode = explode, colors = color, labels = label_list)
plt.legend()
plt.show()

