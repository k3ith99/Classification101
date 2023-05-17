#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np 
import requests
import csv
import json
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display


# In[2]:


#save data into a csv located in same repo
url = "https://www.cryptodatadownload.com/cdd/Bitstamp_BTCUSD_d.csv"
data = pd.read_csv(url)
df = pd.DataFrame(data)
df.to_csv('testing.csv')


# In[12]:


#pull data from csv and organise it into desired dataframe
x = pd.read_csv('testing.csv', header= 1,)
df2 = pd.DataFrame(x)
df2.index = pd.to_datetime(df2['date'])
df3 = pd.DataFrame(df2['close'])
daily_pct_change = df3['close'].pct_change()
df3['daily_pct_change'] = daily_pct_change
weekly_pct_change = df3['close'].pct_change(periods = 5)
df3["weekly_pct_change"] = weekly_pct_change
df3


# In[19]:


#df2['close'].loc["2023"].plot()


# In[54]:


test_data = pd.DataFrame(df3['daily_pct_change'].dropna())


# In[56]:


test_data.reset_index(inplace = True)
sns.lineplot(x = 'date', y = 'daily_pct_change', data = test_data)
plt.show()


# In[41]:


#plt.show()


# In[57]:


#display(df3)


# In[ ]:




