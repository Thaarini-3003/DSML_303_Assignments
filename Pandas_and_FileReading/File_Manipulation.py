import pandas as pd
import json

""" 1. Read CSV file using Pandas"""

df = pd.read_csv('student_habits_performance.csv')
df = pd.DataFrame(df)
print(df.head())
print(df.tail())
print(df[5:10])
print(df[10:])
print(df.loc[4:10])
print(df.iloc[4:10,0:2])
print(df.dtypes)
print(df.describe())
print(df.info())
print(df.shape)
print(df.ndim)
print(df[["student_id"]].head(5))
print(df[["student_id","age","gender"]].head(5))

#read only the column names
column_names = df.columns
print("\n",column_names)

# removing the column which is not in use or which is not needed
df = pd.read_csv("student_habits_performance.csv")
df.drop(columns=["netflix_hours"], inplace=True)
print("\n",df.columns)

# read specific columns of csv file using Pandas
df = pd.read_csv("student_habits_performance.csv", usecols=["student_id", "exam_score"])
print(df)

# Read only the third and last column (indices 2 and 3)
df = pd.read_csv('student_habits_performance.csv', usecols=[2, 3])
print(df)

# Skipping 2 rows from start in csv
# and initialize it to a  dataframe
df = pd.read_csv("student_habits_performance.csv", skiprows = 2)
print("Skip rows", df)

# Skipping rows at specific position
df = pd.read_csv("student_habits_performance.csv", skiprows = [0, 2, 5])
print("Skip rows at specific position")
print(df)

# making data frame from csv file using indexing
data = pd.read_csv("student_habits_performance.csv", index_col ="student_id")

# retrieving row by loc method
first = data.loc["S1000"]
second = data.loc["S1014"]

print(first, "\n\n\n", second)

# Select multiple rows
first = data.loc[["S1000", "S1024"]]
print(first)

# Select two rows and three columns
first = data.loc[["S1000", "S1024"], ["netflix_hours", "extracurricular_participation", "exam_score"]]
print(first)

# Select all rows and specific columns
first = data.loc[:, ["netflix_hours", "extracurricular_participation", "exam_score"]]
print(first)


""" 2. Excel file using Pandas"""

# Import excel file and create DataFrame
df = pd.read_excel('Sample_data.xlsx')
print(df.head())

# Number of sheets
finding_no_of_sheets = df.keys()
print(finding_no_of_sheets)

# Check and Display Specific Column
canada = df[df["Country"] == 'Canada'].head()
print(canada)

Year = df[df["Year"] == 2013].head()
print(Year)

# Reading Specific Columns from an Excel File in Pandas
specific_columns = pd.read_excel("Sample_data.xlsx", usecols="A,C,E,H")
print(specific_columns)

# Selecting a range of columns
range_of_columns = pd.read_excel("Sample_data.xlsx", usecols="A:C")
print(range_of_columns)

# Selecting a range of columns and individual columns
range_and_individual = pd.read_excel("Sample_data.xlsx", usecols="A:C,E")
print(range_and_individual)

# Selecting multiple ranges of columns
multiple_ranges = pd.read_excel("Sample_data.xlsx", usecols="A:C,E:F")
print(multiple_ranges)

#  Using the range() class to read specific columns
range_class = pd.read_excel("Sample_data.xlsx", usecols=range(0,2))
print(range_class)


""" 3. JSON file using Pandas """

df = pd.read_json('data.json')
print(df.head())

data = {"One": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Two": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102}}

json_data = json.dumps(data)

df_normalize = pd.json_normalize(json.loads(json_data))
print("\nDataFrame using JSON module and `pd.json_normalize()` method:")
print(df_normalize)