#!/usr/bin/env python
# coding: utf-8

# # Importing necessary libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv(r"C:\Users\Chandrika\Downloads\titanic\train.csv")  #loading dataset


# In[4]:


df.info() #total information of dataset


# In[5]:


df.head() #first 5 rows of dataset


# In[6]:


df.isnull().sum()


# In[7]:


df.describe()


# # Data Cleaning

# In[8]:


# Handling missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)


# In[9]:


# Verifying no missing values
df.isnull().sum()


# # Research questions:
# 
# 1)What factors influenced the survival rate of passengers on the Titanic?
# 
# 2)How did age and gender affect survival chances?
# 
# 3)What was the survival rate across different passenger classes?

# # Visualization and Analysis
# 

# In[10]:


# 1. Survival rate based on gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival Rate by Gender')
plt.show()


# In[15]:


# 2. Age distribution of survivors vs non-survivors
plt.figure(figsize=(10, 6))
sns.histplot(df[df['Survived'] == 1]['Age'], kde=True, color='green', label='Survived')
sns.histplot(df[df['Survived'] == 0]['Age'], kde=True, color='orange', label='Not Survive')
plt.title('Age Distribution of Survivors vs Non-Survivors')
plt.legend()
plt.show()


# In[16]:


# 3. Survival rate based on passenger class
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title('Survival Rate by Passenger Class')
plt.show()


# In[17]:


# 4. Survival rate based on passenger class and gender
plt.figure(figsize=(10, 6))
sns.catplot(x='Pclass', hue='Sex', col='Survived', data=df, kind='count', height=4, aspect=1.5)
plt.suptitle('Survival Rate by Passenger Class and Gender')
plt.show()


# # conclusion 

# Based on the analysis of the Titanic dataset, we can draw the following conclusions:
# 
# 1. **Gender Influence:** Females had a significantly higher survival rate compared to males.
# 2. **Age Influence:** There is a noticeable difference in the age distribution between survivors and non-survivors, with younger passengers having slightly higher survival rates.
# 3. **Passenger Class Influence:** Passengers in higher classes (First and Second) had a higher survival rate compared to those in Third class.
# 4. **Combined Factors:** The survival rate varies significantly when considering the combination of passenger class and gender, indicating that first-class females had the highest survival rate.
# 
# These insights help us understand the key factors that influenced survival rates during the Titanic disaster.
# 
