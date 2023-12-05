#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("Amazon.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


#drop blanks columns
df.drop(['New','PendingS'],axis=1,inplace=True)


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[10]:


sns.heatmap(df.isnull())
plt.show()


# In[11]:


df.drop(['fulfilled-by'],axis=1,inplace=True)
df.dropna(inplace=True)


# In[12]:


df.isnull().sum()


# In[13]:


df.shape


# In[14]:


df['ship-postal-code']=df['ship-postal-code'].astype(int)


# In[15]:


df.info()


# In[16]:


df['Date']=pd.to_datetime(df['Date'])


# In[17]:


df.info()


# In[18]:


df.head()


# In[36]:


df.rename(columns={'Qty':'Quantity'},inplace=True)


# In[37]:


df.describe()


# In[20]:


df.describe(include=object)


# In[39]:


ax=sns.countplot(x='Size',data=df)
ax.bar_label(ax.containers[0])
plt.show()


# Note:From above graph you can see that most people buys M-size

# In[42]:


df1=df.groupby(["Size"],as_index=False)['Quantity'].sum().sort_values(by='Quantity',ascending=False)
df1


# In[44]:


sns.barplot(x='Size',y='Quantity',data=df1)


# most of quentity buys m-size in the sales

# In[23]:


sns.countplot(x='Courier Status',data=df,hue='Status')


# majorly of the orders are shipped by the courier.

# In[24]:


plt.figure(figsize=(5,5))
sns.displot(df['Size'])
plt.show()


# In[25]:


df['Category']=df['Category'].astype(str)
df['Category']


# In[26]:


df.info()


# In[47]:


plt.hist(df['Category'],bins=30,color='olive',edgecolor='black')
plt.xticks(rotation=45)
plt.show()


# most of the buyers are T-shart and shart

# In[28]:


p=df['B2B'].value_counts(normalize=True)
p


# In[30]:


plt.pie(p,labels=p.index,autopct='%0.2f%%')
plt.show()


# In[53]:


plt.figure(figsize=(8,5))
sns.scatterplot(x='Category',y='Size',data=df,color='brown')
plt.show()


# In[32]:


plt.figure(figsize=(10,5))
sns.countplot(x='ship-state',data=df)
plt.xticks(rotation=90)
plt.show()


# In[33]:


h=df['ship-state'].value_counts()[0:5]
h


# In[34]:


v=list(df['ship-state'].value_counts()[0:5].keys())
v


# In[35]:


plt.figure(figsize=(10,5))
plt.bar(v,h,color='g',edgecolor='black')
plt.show()


# most of buyers are maharashtra state

# # conclusion

# The data analysis reveals that the business has a significant customer base in maharastra state ,mainly serves retailers,
# fulfills orders through amazon,experiences high demand for T-sharts,and see M-size as the preferrs most of buyers.

# In[ ]:




