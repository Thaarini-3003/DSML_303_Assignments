import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns

#1. Reading the CSV file
df = pd.read_csv("Salary_Data.csv")
print(df.head(10))
print("\n")
datatype = df.dtypes

#2. Initial data
shape = df.shape

# 3. Finding Null in the dataset
null_data = df.isna().sum()

# 4. Data Distribution of YearsExperience
sns.histplot(df['YearsExperience'], kde=True)
plt.title('Distribution of Years of Experience')
plt.show()

#5. Data Distribution of Salary
sns.histplot(df['Salary'], kde=True)
plt.title('Distribution of Salary')
plt.show()

# 6. Finding outliers
sns.scatterplot(x=df["YearsExperience"],y=df["Salary"])
plt.show()

# 7. Correlation matrix
correlation_matrix= df.corr()
print("\nCORRELATION MATRIX \n",correlation_matrix)

# 8. Model selection (linearRegression) Split and train data
X = df[["YearsExperience"]]
y= df["Salary"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)

# 9. Prediction
# print(X_test,y_test)
y_pred =model.predict(X_test)
print("\ny_Prediction", y_pred)

# 10. Metrics - Accuracy check
testing_accuracy = r2_score(y_test,y_pred)
print("\nAccuracy R2-score :", testing_accuracy)

# 11. Future Prediction
model1 = LinearRegression()
model1.fit(X,y)
prediction = model.predict(pd.DataFrame({"YearsExperience":[11,11.5,12.7,13.8,14.0,15.2]}))
print("\nFinal Prediction for new set YearsExperience {[11,11.5,12.7,13.8,14.0,15.2]}\n:", prediction)