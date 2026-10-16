from sklearn.datasets import make_blobs #Generates artificial datasets containing groups of points called clusters
import matplotlib.pyplot as plt
import numpy as np
from kmeans import Kmeans #Importing the Kmeans class

centroids = [(-5,-5),(7,7)] #Center of the clusters
cluster_std = [2,2] #Standard deviation of the clusters

X,y = make_blobs(n_samples=100,cluster_std=cluster_std,centers=centroids,n_features=2)


km = Kmeans(n_clusters=2,max_iters=100)
km.fit_predict(X)

