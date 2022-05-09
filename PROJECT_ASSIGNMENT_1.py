# ## PROJECT ASSIGNMENT 1

# necessary imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


# **Some of the Hypothesis are :-**
# - For larger bill tip will also be large.
# - tips will be higher during weekends.
# - At Dinner Time tips will be higher than in lunch Time.

# In[2]:


# reading data 

df = pd.read_csv('tips.csv')
df.head() # looking at the first five rows of dataset

df.shape

df.info()


df.describe()

df.isna().sum()

# encoding categorical columns

df['sex'] = df['sex'].map({'Female': 0, 'Male':1})
df['smoker'] = df['smoker'].map({'No': 0, 'Yes':1})
df['time'] = df['time'].map({'Dinner': 0, 'Lunch': 1})
df['day'] = df['day'].map({'Sat': 1, 'Sun': 2, 'Thu': 3, 'Fri': 4})



df.head()

plt.figure(figsize = (15, 6))
plt.scatter(x = df['total_bill'], y = df['tip'])
plt.title('Tips vs Total Bill\n', fontsize = 15)
plt.xlabel('Total Bill')
plt.ylabel('Tips')
plt.show()

day_tips = df.groupby(['day'])['tip'].sum()
day_tips

plt.figure(figsize = (13, 6))
day_tips.plot()
plt.xticks([1, 2, 3, 4])
plt.title('Tips per Day\n', fontsize = 15)
plt.ylabel('Tips')
plt.show()

time_tips = df.groupby(['time'])['tip'].sum()

plt.figure(figsize = (10, 6))
time_tips.plot()

plt.xticks([0, 1])
plt.title('Tips as per Time\n', fontsize = 15)
plt.ylabel('Tips')
plt.show()


# ## Findings 

# - We can conclude from tips vs total scatter plot bill, that the customers who paid lower bills gave lower tips but customers who had high bill had given high tips.
# - On weekend tips were high.
# - On a particular day tips were high during Dinner.
