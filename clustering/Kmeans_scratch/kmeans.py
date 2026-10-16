class Kmeans:
    def __init__(self,n_clusters=2,max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.centrodis  =None
    
    def fit_predict(self,X):
        print(X)

