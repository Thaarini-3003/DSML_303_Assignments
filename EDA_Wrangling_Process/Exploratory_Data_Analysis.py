import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

happinessData = pd.read_csv('World_Happiness_Report.csv')
print(happinessData.head())
print("-------------------------")
print("-------------------------")
print(f"Shape of the data: {happinessData.shape}")
print("-------------------------")
print("-------------------------")
print(happinessData.info())
print(happinessData.describe())

# handle the missing values
print(happinessData.isnull().sum())
happinessData.fillna(happinessData['Happiness Score'].mean(),inplace=True)
happinessData.fillna(happinessData['Freedom'].mean(),inplace=True)
print(happinessData.isnull().sum())


# check for duplicate values
print(happinessData.duplicated().sum())

happinessData.boxplot(column=["Happiness Score"])
plt.show()

q1 = np.quantile(happinessData["Happiness Score"],0.25)
print(q1)

q3 = np.quantile(happinessData["Happiness Score"],0.75)
print(q3)

IQR = q3 - q1
print(IQR)

lower_range = q1 - 1.5 * IQR
higher_range = q3 + 1.5 * IQR
print(lower_range)
print(higher_range)
# final_data = []
happinessData['Happiness Score'] = np.where(happinessData["Happiness Score"]>higher_range, higher_range, happinessData['Happiness Score'])
happinessData['Happiness Score'] = np.where(happinessData['Happiness Score']<lower_range, lower_range, happinessData['Happiness Score'])


happinessData.boxplot(column=["Happiness Score"])
plt.show()

stdScale = StandardScaler()
happinessData["Happiness Score"] = stdScale.fit_transform(happinessData[["Happiness Score"]])
# print(happinessData["Happiness Score"].head())

# sns.heatmap(happinessData.corr(), annot=True, cmap="RdY1Gn")
sns.regplot(x='Economy (GDP per Capita)',y="Happiness Score", data=happinessData)
plt.title('Regression Plot using Seaborn')
plt.show()

sns.regplot(x='Family',y="Happiness Score", data=happinessData)
plt.title('Regression Plot using Seaborn')
plt.show()

sns.regplot(x='Health (Life Expectancy)',y="Happiness Score", data=happinessData)
plt.title('Regression Plot using Seaborn')
plt.show()