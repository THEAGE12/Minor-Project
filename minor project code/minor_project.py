# -*- coding: utf-8 -*-
"""Minor Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BaImJcQaRUTepo-A7OtKXeGSLaeNoBZJ
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import StandardScaler
from yellowbrick.cluster import KElbowVisualizer
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
# %matplotlib inline
sns.set_style('whitegrid')
plt.style.use('fivethirtyeight')

dataset = pd.read_csv("/content/log_temp.csv")
dataset.head()
dataset = dataset.dropna()

dataset1 = pd.read_csv("/content/dataset.csv")
dataset1.head()
x = dataset1.iloc[:, [1, 5]].values
x

dataset1 = pd.read_csv("/content/plant_vase1.CSV")
dataset1.head()
x = dataset1.iloc[:, [6, 10]].values
x

dataset['T=22.0'] =pd.to_numeric (dataset['T=22.0'].str.replace(r'\D+', '', regex=True))
dataset['T=22.0']=[y//10 for y in dataset['T=22.0']]
dataset['H=20.0'] = pd.to_numeric(dataset['H=20.0'].str.replace(r'\D+', '', regex=True))
dataset['H=20.0']=[y//10 for y in dataset['H=20.0']]
x = dataset.iloc[:, [2, 3]].values
x

import matplotlib.pyplot as mtp
from sklearn.cluster import KMeans
wcss_list= []  #Initializing the list for the values of WCSS

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state= 42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)
mtp.plot(range(1, 11), wcss_list)
mtp.title('The Elobw Method Graph')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

kmeans = KMeans(n_clusters=3, init='k-means++', random_state= 42)
y_predict= kmeans.fit_predict(x)

dataset1.info()

km = KMeans(n_clusters=5)
y_predicted = km.fit_predict(dataset1[['moisture0', 'moisture1', 'moisture2', 'moisture3', 'moisture4']])
y_predicted

dataset1["Cluster"] = y_predicted
dataset1.head(1000)

mtp.scatter(x[y_predict== 2, 0], x[y_predict == 2, 1], s = 100, c = 'red', label = 'Cluster 1') #for third cluster
mtp.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s = 100, c = 'cyan', label = 'Cluster 2') #for fourth cluster
mtp.scatter(x[y_predict == 4, 0], x[y_predict == 4, 1], s = 100, c = 'magenta', label = 'Cluster 3') #for fifth cluster
mtp.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroid')
mtp.title('Clusters of IOT DATA')
mtp.xlabel('')
mtp.ylabel('')
mtp.legend()
mtp.show()

import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster import hierarchy
plt.figure(figsize=(17,10))
plt.title('Dendrogram')
plt.xlabel('Temperature')
plt.ylabel('Euclidean distances')
#plt.grid(True)
dendrogram = sch.dendrogram(sch.linkage(x, method = 'ward'))
plt.show()

plt.figure(figsize=(15,6))
plt.title('Dendrogram')
plt.xlabel('Data')
plt.ylabel('Euclidean distances')
plt.hlines(y=5,xmin=0,xmax=19000,lw=3,linestyles='--')
plt.text(x=60,y=5,s='Horizontal line crossing 4 vertical lines',fontsize=20)
#plt.grid(True)
dendrogram = sch.dendrogram(sch.linkage(x, method = 'ward'))
plt.show()

# Commented out IPython magic to ensure Python compatibility.
from sklearn.cluster import DBSCAN
import sklearn.utils
from sklearn.preprocessing import StandardScaler
# %matplotlib inline
Clus_dataSet = x
Clus_dataSet = np.nan_to_num(Clus_dataSet)
Clus_dataSet = np.array(Clus_dataSet, dtype=np.float64)
Clus_dataSet = StandardScaler().fit_transform(Clus_dataSet)
# Compute DBSCAN
db = DBSCAN(eps=0.4, min_samples=5).fit(Clus_dataSet)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
dataset['Clus_Db']=labels
realClusterNum=len(set(labels)) - (1 if -1 in labels else 0)
clusterNum = len(set(labels))
# A sample of clusters
print(dataset.head())
# Number of Labels
print("number of labels: ", set(labels))

plt.figure(figsize=(15,10))
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:

        # Black used for noise.
        col = [0, 0, 0, 1]
class_member_mask = (labels == k)
xy = Clus_dataSet[class_member_mask & core_samples_mask]
plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=14)
xy = Clus_dataSet[class_member_mask & ~core_samples_mask]
plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=6)
plt.title('Clustering of Customers, Estimated Number of Clusters: %d' % realClusterNum, fontweight='bold',fontsize=20)
plt.xlabel('Annual Income',fontsize=20)
plt.ylabel('Spending Score',fontsize=20)
plt.legend(fontsize=20)
plt.show()
n_noise_ = list(labels).count(-1)
print('number of noise(s): ', n_noise_)

