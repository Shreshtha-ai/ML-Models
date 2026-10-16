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
            old_centroids  =self.centroids
            self.centroids =self.move_centroids(X,cluster_group)

            if(old_centroids.all()==self.centroids.all()):
                break
        
        return cluster_group
    

    def assign_clusters(self,X):
        cluster_group = []
       

        for row in X:
            distances = []
            for centroid in self.centroids:
               distances.append(np.sqrt(np.dot(row-centroid,row-centroid)))
               min_distance = min(distances)
               index_pos = distances.index(min_distance)
               cluster_group.append(index_pos)

               print(index_pos) 
               
            
        return np.array(cluster_group)

    def move_centroids(self,X,cluster_group):
        new_centroids = []
        cluster_type = np.unique(cluster_group)

        for type in cluster_type:
            new_centroids.append(X[cluster_group ==type].mean(axis=0)) # for calculating mean for each cluster type along the columns

        return np.array(new_centroids) 
            



            


    

