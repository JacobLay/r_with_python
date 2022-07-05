#!/usr/bin/env python
# coding: utf-8

# # Linear Regression Homework in Python

# ## Data Import from regrex1.csv

# In[1]:


#Importing the dataset
import pandas as pd
import sys
dataset = pd.read_csv(sys.argv[1])


# ## Generation of Linear Regression Model

# In[2]:


# Fitting Linear Regression to the Dataset
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[['x']], dataset[['y']])


# ## Calculation of R-Square from Linear Regression Model

# In[3]:


#Adjusted R-squared
model.score(dataset[['x']], dataset[['y']])


# ## Creation of Graph from regrex.csv Data Points and Linear Regression Model

# In[4]:


#Visualizing the Linear Regression results
import matplotlib.pyplot as plt
plt.scatter(dataset[['x']], dataset[['y']], color = 'red')
# plt.plot(dataset[['x']], model.predict(dataset[['x']]), color = 'blue')
plt.title('y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('py_orig.png')
plt.plot(dataset[['x']], model.predict(dataset[['x']]), color = 'blue')
plt.savefig('py_lm.png')
plt.clf()