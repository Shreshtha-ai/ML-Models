import random
import numpy as np

class Kmeans:
    def __init__(self,n_clusters=2,max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.centroids  =None
    
    def fit_predict(self,X):
        random_index  =(random.sample(range(0,X.shape[0]),self.n_clusters))
        self.centroids = X[random_index]
        print(self.centroids)

        for i in range(self.max_iters):
            cluster_group = self.assign_clusters(X)
    

    def assign_clusters(self,X):
        cluster_group = []
       

        for row in X:
            distances = []
            for centroid in self.centroids:
               distances.append(np.sqrt(np.dot(row-centroid,row-centroid)))
               print(distances) 
               
            
        return cluster_group


            


    

