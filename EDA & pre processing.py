#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df= pd.read_excel(r'C:\Users\user\Desktop\Assignment OR Portfolio datasets\Medical Inventory Optimaization Dataset.xlsx')


# In[3]:


#1 Understanding the data
df.head()


# In[4]:


df.tail()


# In[5]:


print(df.shape)


# In[6]:


df.columns


# In[7]:


df.nunique()


# In[8]:


#Cleaning the data
df.isnull().sum()


# In[9]:


print(df['Formulation'].mode())
print(df['DrugName'].mode())
print(df['SubCat'].mode())
print(df['SubCat1'].mode())


# In[10]:


new_df = df.copy()


# In[11]:


df['DrugName'].mode()
new_df['DrugName'] = df ['DrugName'].fillna(df['DrugName'].mode())


# In[12]:


df['SubCat'].mode()
new_df['SubCat'] = df ['SubCat'].fillna(df['SubCat'].mode())


# In[13]:


df['Formulation'].mode()
new_df['Formulation'] = df ['Formulation'].fillna(df['Formulation'].mode())


# In[14]:


df['SubCat1'].mode()
new_df['SubCat1'] = df ['SubCat1'].fillna(df['SubCat1'].mode())


# In[15]:


new_df.isnull().sum()


# In[16]:


df.duplicated().sum()


# In[17]:


data = pd.DataFrame(df)
display(data.drop_duplicates())


# In[18]:


medical = df.drop(['RtnMRP'], axis = 1)
medical.head()


# In[19]:


#relationship analysis
df.describe()


# In[20]:


df.corr()


# In[21]:


sns.pairplot(df)


# # IQR

# In[22]:


sns.catplot(y = 'Quantity', kind = 'box', data =df)


# In[23]:


Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1
print(Q1, Q3, IQR)


# In[24]:


upper_limit = Q3 + (1.5*IQR)
lower_limit = Q1 - (1.5*IQR)
print(lower_limit, upper_limit)


# In[25]:


#trimming - delete the outlier data
new_df = df[(df['Quantity']< upper_limit) & (df['Quantity'] > lower_limit)]
print('Before removing outliers:', len(df))
print('After removing Outliers:', len(new_df))
print('outliers:', len(df)-len(new_df))


# In[26]:


sns.boxplot(new_df['Quantity'])


# In[27]:


sns.catplot(y = 'Final_Sales', kind = 'box', data =df)


# In[28]:


Q1 = df['Final_Sales'].quantile(0.25)
Q3 = df['Final_Sales'].quantile(0.75)
IQR = Q3 - Q1
print(Q1, Q3, IQR)


# In[29]:


upper_limit1 = Q3 + (1.5*IQR)
lower_limit1 = Q1 - (1.5*IQR)
print(lower_limit1, upper_limit1)


# In[30]:


#trimming - delete the outlier data
new_df = df[(df['Final_Sales']< upper_limit1) & (df['Final_Sales'] > lower_limit1)]
print('Before removing outliers:', len(df))
print('After removing Outliers:', len(new_df))
print('outliers:', len(df)-len(new_df))


# In[31]:


sns.boxplot(new_df['Final_Sales'])


# In[32]:


sns.catplot(y = 'Final_Cost', kind = 'box', data =df)


# In[33]:


Q1 = df['Final_Cost'].quantile(0.25)
Q3 = df['Final_Cost'].quantile(0.75)
IQR = Q3 - Q1
print(Q1, Q3, IQR)


# In[34]:


upper_limit2 = Q3 + (1.5*IQR)
lower_limit2 = Q1 - (1.5*IQR)
print(lower_limit2, upper_limit2)


# In[35]:


#trimming - delete the outlier data
new_df = df[(df['Final_Cost']< upper_limit2) & (df['Final_Cost'] > lower_limit2)]
print('Before removing outliers:', len(df))
print('After removing Outliers:', len(new_df))
print('outliers:', len(df)-len(new_df))


# In[36]:


sns.boxplot(new_df['Final_Cost'])


# In[37]:


plt.bar('Quantity', data= df, color ='g', height = 1)
plt.title('Quantity Bar Graph')
plt.xlabel('Quantity')
plt.ylabel('Density')
plt.show()


# In[38]:


plt.scatter('Final_Sales','Final_Cost', data= df, color ='red')
plt.title('Scatter Plot')
plt.xlabel('Final_Sales')
plt.ylabel('Final_Cost')
plt.show()


# In[ ]:




