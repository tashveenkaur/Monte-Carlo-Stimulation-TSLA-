#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df=yf.download("TSLA")


# In[4]:


returns = np.log(1+df['Adj Close'].pct_change())


# In[6]:


mu , sigma = returns.mean(),returns.std() 


# In[16]:


sim_rets = np.random.normal(mu,sigma,252)


# In[17]:


initial = df['Adj Close'].iloc[-1]


# In[18]:


initial 


# In[19]:


sim_prices = initial*(sim_rets+1).cumprod()


# In[20]:


plt.plot(sim_prices)


# In[29]:


for i in range(200):
    sim_rets = np.random.normal(mu,sigma,252)
    sim_prices = initial*(sim_rets+1).cumprod()
    plt.axhline(initial,c='Black')
    plt.plot(sim_prices)


# In[ ]:




