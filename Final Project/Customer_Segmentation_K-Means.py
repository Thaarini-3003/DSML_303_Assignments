import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


pd.set_option("display.max_columns",None)


# Step 1. Load the dataset
df = pd.read_csv("Customer_Order_Details.csv")
# print(df.head())

# Step 2. Get insights on Dataset
print(df.info())
print(df.shape)

# Step 3. Drop unused columns
df.drop(columns=['master_id','interested_in_categories_12'], inplace=True)

# Step 4. Rename the columns for Readability
df = df.rename(columns={'order_channel' : 'Registered_Channel',
                        'last_order_channel': 'Recent_order_Channel',
                        'order_num_total_ever_online': 'Total_Online_Orders',
                        'order_num_total_ever_offline': 'Total_Offline_Orders',
                        'customer_value_total_ever_offline': 'Gross_value_Offline',
                        'customer_value_total_ever_online': 'Gross_value_Online'})


# Step 5. Finding duplicates
duplicates = df[df.duplicated()]
# print(duplicates)


# Step 6. Finding Null
print(df.isnull().sum())


# Step 7. Convert the date columns from string datatype to datetime64[ns]
date_columns = df.columns[df.columns.str.contains("date")]
df[date_columns] = df[date_columns].apply(pd.to_datetime)


# Step 8. Calculate the tenure and recency of purchase
# print(df["last_order_date"].max())  # 2021-05-30
today_date = dt.datetime(2021, 6, 1) # setting the current date as next day of (2021-05-30)
df["tenure"] = (df["last_order_date"] - df["first_order_date"]).dt.days
df["recency"] = (today_date - df["last_order_date"]).dt.days

# Step 9. Visualize the Distribution of data
plt.title("Distribution of Registered Channel")
plt.hist(df.Registered_Channel)
plt.show()

plt.title("Distribution of Recent order Channel")
plt.hist(df.Recent_order_Channel)
plt.show()

plt.title("Distribution of Last order date Offline")
plt.hist(df.last_order_date_offline)
plt.show()

plt.title("Distribution of Last order date Online")
plt.hist(df.last_order_date_online)
plt.show()


# Step 10. Creating a new dataset for model
model_df = df[["Total_Online_Orders", "Total_Offline_Orders", "Gross_value_Offline", "Gross_value_Online", "tenure", "recency"]]


# Step 11. Checking the correlation between the columns
correlation_matrix= model_df.corr()
sns.heatmap(correlation_matrix, cmap="magma", annot=True)
plt.show()


# Step 12. Scaling the features using Standard Scaler (numerical columns)
standard_scaler = StandardScaler()
numerical = model_df.select_dtypes(include='float64').columns
model_df.loc[:,numerical] = standard_scaler.fit_transform(model_df.loc[:,numerical])
X_scaled = model_df.copy()



# Step 13. The elbow Method for PCA to determine the number of clusters
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Cumulative explained variance
print("\n Explained Variance ratio :",pca.explained_variance_ratio_)
# plot graph
plt.figure(figsize=(10,8))
plt.plot(range(1,7), pca.explained_variance_ratio_.cumsum(), marker='o')
plt.axhline(y=0.95, color='r', linestyle='--')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance vs Number of Components')
plt.grid(True)
plt.show()

# Step 14. Reduce Dimensionality using PCA
pca = PCA(n_components=2)
scores_pca = pca.fit_transform(X_scaled)
print("\n PCA Scores :", scores_pca)


# Step 15: Create a DataFrame with PCA results
df_pca = pd.DataFrame(data=scores_pca, columns=['PC1', 'PC2'])
print("\n PCA - Explained variance ratio: ",pca.explained_variance_ratio_)
# # print(df_pca)
# Step 5: Plot the PCA results
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b']
cluster_labels = ['PC1', 'PC2']
for i in range(2):
    plt.scatter(df_pca['PC1'],
                df_pca['PC2'],
                s=10, color=colors[i],
                label=f'{cluster_labels[i]}')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Dataset')
plt.legend()
plt.grid(True)
plt.show()


# Step 16. The elbow Method for KMeans to determine the number of clusters
wcss = {}
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(scores_pca)
    wcss[i] = kmeans.inertia_

plt.plot(wcss.keys(), wcss.values(), 'gs-')
plt.xlabel("Values of 'k'")
plt.ylabel('WCSS')
plt.title("Determine KMeans Cluster")
plt.grid(True)
plt.show()

# Step 17: Apply K-Means clustering
kmeans_pca = KMeans(n_clusters=2, init='k-means++', random_state=42)
kmeans_pca.fit(scores_pca)
labels = kmeans_pca.labels_
print("\n Kmeans labels:",labels)
print("\n Kmeans-Cluster centers :",kmeans_pca.cluster_centers_)
# df_pca = pd.DataFrame(data=df_Kmeans, columns=['Kmeans1', 'Kmeans2'])

cust_segn_pca_kmeans = pd.concat([df.reset_index(drop = True), pd.DataFrame(scores_pca)], axis =1)
cust_segn_pca_kmeans.columns.values[-2:] = ['Component 1', 'Component 2']

cust_segn_pca_kmeans["Segment K-means PCA"] = kmeans_pca.labels_
print(cust_segn_pca_kmeans.head())

cust_segn_pca_kmeans['Segment'] = cust_segn_pca_kmeans['Segment K-means PCA'].map({0:'first',
                                                                                   1:'Second',
                                                                                   2:'third'
                                                                                   })
# print(cust_segn_pca_kmeans)


# Step 18: Scatter plot for Cluster
#Plot data by PCA components. The Y axis is the first component, Xaris is the second.
x_axis = cust_segn_pca_kmeans["Component 2"]
y_axis =  cust_segn_pca_kmeans["Component 1"]
plt.figure(figsize = (10, 8))
sns.scatterplot(x=x_axis, y=y_axis, hue=cust_segn_pca_kmeans['Segment'], palette =['g','r'])
plt.title('Clusters by PCA Components')
plt.show()


# Step 19: Bar graph based on channel
summed_values = df.groupby('Recent_order_Channel')['Gross_value_Online'].sum()
# Round the sums to 2 decimal places
summed_values_rounded = summed_values.round(2)
# Plot the bar graph
summed_values_rounded.plot(kind='bar', color='skyblue')
plt.title('Summed Values by Channel')
plt.xlabel('Category')
plt.ylabel('Gross amount')
plt.show()



# Step 20 : Grouped Bar Plot
summed_values1 = df.groupby('Recent_order_Channel')['Gross_value_Online'].sum().round(2)
summed_values2 = df.groupby('Recent_order_Channel')['Gross_value_Offline'].sum().round(2)
bar_width = 0.35
x = np.arange(len(df['Recent_order_Channel'].unique()))
plt.bar(x - bar_width/2, summed_values1, bar_width, label='Online purchase', color='skyblue')
plt.bar(x + bar_width/2, summed_values2, bar_width, label='Offline Purchase', color='lightgreen')

# Adding labels and title
plt.xlabel('Recent order by channel')
plt.ylabel('Online or Offline Purchase')
plt.title('Channel Preferences by Customer')
plt.xticks(x, df['Recent_order_Channel'].unique())
plt.legend(title='Channel')
plt.show()

print("***************Customer Segmentation with RFM Metrics*********************************")

# Load CSV
df = pd.read_csv("Customer_Order_Details.csv")
date_columns = df.columns[df.columns.str.contains("date")]
df[date_columns] = df[date_columns].apply(pd.to_datetime)

# Total orders and total customer value
df["total_order"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["total_customer_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
# print(df.head())


print(df.groupby("order_channel").agg({"master_id": "count",
                                 "total_order": "sum",
                                 "total_customer_value": "sum"}))


rfm = df.groupby("master_id").agg({"last_order_date": lambda x: (today_date-x.max()).days,
                                   "total_order": lambda x: x.max(),
                                   "total_customer_value": lambda x: x.max()})
rfm.reset_index(inplace=True)
print(rfm.head())

rfm.columns = ["master_id", "recency", "frequency", "monetary"]
# print(rfm.head())

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])

rfm["RF_SCORE"] = rfm["recency_score"].astype("str") + rfm["frequency_score"].astype("str")

seg_map = {
    r"[1-2][1-2]": "hibernating",
    r"[1-2][3-4]": "at_risk",
    r"[1-2]5": "cant_loose",
    r"3[1-2]": "about_to_sleep",
    r"33": "need_attention",
    r"[3-4][4-5]": "loyal_customers",
    r"41": "promising",
    r"51": "new_customers",
    r"[4-5][2-3]": "potential_loyalists",
    r"5[4-5]": "champions",
}

rfm["SEGMENT"] = rfm["RF_SCORE"].replace(seg_map, regex=True)
print(rfm.head())

print(rfm.groupby("SEGMENT").agg({'recency': ["mean", "count"],
                            'frequency': ["mean", "count"],
                            'monetary': ["mean", "count"]}))












