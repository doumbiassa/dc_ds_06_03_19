#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


cols = ['year', 'month', 'decimalyear', 'average','interpolated', 'trend', '#days']


# In[32]:


df = pd.read_csv("ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt", delim_whitespace=True, header=None, comment="#", names=cols)


# In[33]:


df.head()


# In[34]:


df.columns =  ["year", "month", "decimalYear", "co2", "interpolated", "trend", "num_days"]


# In[35]:


df.head(2)


# In[36]:


df.iloc[:,[0,1,3]].head(2)


# In[37]:


df.head(2)


# In[38]:


# Version using just pandas
#df[df['co2'] == -99.99] = np.NaN


# In[39]:


# Version using just np.where
df.co2 = np.where(df["co2"] == -99.99, np.NaN, df["co2"])


# In[40]:


df.head()


# In[41]:


df['day'] = 15


# In[42]:


df1 = df.iloc[:, [0,1,3,7]]


# In[43]:


df1.head()


# In[45]:


s = ['year', 'month']


# ### Dummies__Variables

# In[49]:


pd.get_dummies(data=df1, columns=['year', 'month']).head(5)


# In[52]:


def normalize_func(df):
    return ((df-np.mean(df))/np.std(df))
    


# In[54]:


normalize_func(df1['co2']).hist()


# In[ ]:




