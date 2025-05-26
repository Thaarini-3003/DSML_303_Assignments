import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Titanic-Dataset.csv')
# print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

# Get Info
print("\n Duplicates :",df.duplicated().sum())
print("\n", df.info()) #  Age, Cabin and Embarked have an unequal number of counts (have null values)
sns.heatmap(df.isna())


# check the Categorical columns ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
cat_col = [col for col in df.columns if df[col].dtype == 'object']
print('Categorical columns :',cat_col)

# check the Numerical columns ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
num_col = [col for col in df.columns if df[col].dtype != 'object']
print('Numerical columns :',num_col)

# Check the total number of Unique Values in the Categorical Columns
print("\n Unique values in categorical columns : \n", df[cat_col].nunique())
# print(df['Ticket'].unique()[:50])

# Drop Name and Ticket column ( these categorical cols have no impact on target)
df1 = df.drop(columns=['Name','Ticket'])  #New DataFrame df1 from this step
print(df1.shape)

# Handling Null values
print(df1.isnull().sum())

"""Cabin has 687 null values which cannot be filled, so drop the "column"
Embarked has 2 null values, so drop those 2 rows alone in Embarked column"""
df2 = df1.drop(columns='Cabin')
df2.dropna(subset=['Embarked'], axis=0, inplace=True)
print(df2.shape)
# print(df2.isnull().sum())


# Mean imputation
df3 = df2.fillna(df2.Age.mean())
# Let's check the null values again
print(df3.isnull().sum())


# EDA ---> finding outliers
plt.boxplot(df3['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
plt.show()

