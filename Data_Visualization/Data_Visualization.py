import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Line Graph

yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(yield_apples)
plt.show()

years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(years,yield_apples)
plt.xlabel("Year")
plt.ylabel("Yield (Tons per Hectare)")
plt.show()

years = range(2000, 2012)
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
yield_oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years,yield_apples, marker='o')
plt.plot(years,yield_oranges, marker='x')
plt.xlabel("Year")
plt.ylabel("Yield (Tons per Hectare)")
plt.title("Crop Yields in India")
plt.legend(['Apples','Oranges'])
plt.show()


sns.set_style("whitegrid")
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
yield_oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years,yield_apples, marker='o')
plt.plot(years,yield_oranges, marker='x')
plt.xlabel("Year")
plt.ylabel("Yield (Tons per Hectare)")
plt.title("Crop Yields in India")
plt.legend(['Apples','Oranges'])
plt.show()


# 2. Bar Graph

years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
plt.bar(years, oranges)
plt.xlabel('Year')
plt.ylabel('Yield of Oranges(tons per hectare)')
plt.title("Crop Yields in India")
plt.show()


plt.bar(years,apples)
plt.bar(years,oranges, bottom=apples)
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')
plt.title("Crop Yields in India")
plt.legend(['Apples','Oranges'])
plt.show()


tips_df = sns.load_dataset("tips")
print(tips_df)

sns.barplot(x='day', y='total_bill', data=tips_df)
plt.show()

sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df)
plt.show()

sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df)
plt.show()


# 3. Histogram

flowers_df = sns.load_dataset("iris")
print(flowers_df.sepal_width)

plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width)
plt.show()


plt.hist(flowers_df.sepal_width, bins=5)
plt.show()

plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25))
plt.show()


setosa_df= flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.show()

plt.title('Distribution of Sepal Width')
plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],bins=np.arange(2, 5, 0.25),
stacked=True)
plt.legend(['Setosa', 'Versicolor', 'Virginica'])
plt.show()


# 4. Scatter plot

flowers_df = sns.load_dataset("iris")
# print(flowers_df.sepal_width)

flowers_df.species.unique()

plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
plt.show()

sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width)
plt.show()

sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=70)
plt.show()


# 5. Heat Maps

flights_df = sns.load_dataset("flights").pivot(columns=["month"])
print(flights_df)


plt.title("No. of passengers (1000s) ")
sns.heatmap(flights_df)
plt.show()

# Example: Heatmap
data = np.random.rand(10, 12)
sns.heatmap(data, cmap='viridis')
plt.title('Heatmap Example')
plt.show()


# 6. Pie chart

data = [15, 25, 25, 30, 5]
labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']

colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%', explode = [0, 0, 0, 0.2, 0])
plt.title("Pie chart")
plt.show()

# 7. Radar chart

import matplotlib.pyplot as plt
import numpy as np
# Example: Radar Chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 2, 5, 3, 1]
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
values += values[:1]
# Ensure that angles array has the same length as values
angles = np.concatenate((angles, [angles[0]]))
plt.polar(angles, values, marker='o')
plt.title('Radar Chart Example')
plt.show()


# 8 . AREA chart

import matplotlib.pyplot as plt
# Example: Area Chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.fill_between(x, y, color='skyblue', alpha=0.4)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Area Chart Example')
plt.show()

