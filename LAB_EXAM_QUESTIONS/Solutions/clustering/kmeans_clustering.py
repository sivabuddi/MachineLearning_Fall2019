'''
problem 6 : Applying K Means regression Technique
a. Report which K is the best using the elbow method.
b.  Evaluate  with  silhouette  score  or  other  scores  relevant  for  unsupervised approaches (before applying
clustering clean the data set with the EDA learned in the class)

'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn import metrics

college_data = pd.read_csv("./College.csv")
print(college_data.isnull().sum())
corr_matrix = college_data.corr()
print(corr_matrix["Grad.Rate"].sort_values(ascending=False))

print(college_data.isnull().sum())
sns.FacetGrid(college_data, hue="Grad.Rate", height=4).map(plt.scatter, "Expend", "Grad.Rate").add_legend()
plt.show()

college_data['Private'] = college_data['Private'].map({'Yes': 1, 'No': 0})
college_data = college_data.drop(['University'], axis=1)

print("Original Data size=", college_data.shape)
x = college_data.iloc[:, 1:17]
y = college_data.iloc[:, -1]
print(x.shape, y.shape)

scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns=x.columns)

nclusters = 3  # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(x)

score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)

# ##elbow method to know the number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()
print("finished")
