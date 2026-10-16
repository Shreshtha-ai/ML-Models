from sklearn.datasets import make_blobs #Generates artificial datasets containing groups of points called clusters
import matplotlib.pyplot as plt
import numpy as np
from kmeans import KMeans #Importing the Kmeans class

centroids = [(-5,-5),(7,7)] #Center of the clusters
cluster_std = [2,2] #Standard deviation of the clusters

X,y = make_blobs(n_samples=100,cluster_std=cluster_std,centers=centroids,n_features=2)


km = KMeans(n_clusters=2,max_iter=100)
y_means = km.fit_predict(X)
plt.scatter(X[y_means==0,0],X[y_means==0,1],label="cluster1",color="red")
plt.scatter(X[y_means==1,0],X[y_means==1,1],label="cluster2",color="blue")
plt.legend()
plt.show() 

