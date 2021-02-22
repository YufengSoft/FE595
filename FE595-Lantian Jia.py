#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt


# In[25]:


x=np.arange(0,2*np.pi,0.01)
y1=np.sin(x)
y2=np.cos(x)


# In[32]:


plt.title('plot of sinx and cosx') 
plt.plot(x,y1,color="blue")
plt.plot(x,y2,color="red")
plt.legend(['y=sinx','y=cosx'])


# In[ ]:




