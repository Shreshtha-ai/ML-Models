import numpy as np

class AgglomerativeClustering:
    def __init__(self,n_cluster=2):
        self.n_cluster = n_cluster
    

    def fit_predict(self,X):
        n = len(X)

        cluster = []

        for i in range(n):
            cluster.append([X[i]])
        
        dist = np.zeros((n,n))
        for i in range(n):
            for j in range(i+1,n):
                dist[i][j] = dist[j][i] = np.sqrt(np.sum((X[i]-X[j])**2))
    
        while (len(cluster) > self.n_cluster):
            min_dist = float("inf")
            pair = None

            for i in range(len(cluster)):
                for j in range(i + 1, len(cluster)):
                    d = min(
                        np.linalg.norm(p1 - p2)
                        for p1 in cluster[i]
                        for p2 in cluster[j]
                    )

                    if d < min_dist:
                        min_dist = d
                        pair = (i, j)

            i, j = pair

            cluster[i] += cluster[j]
            cluster.pop(j)

        labels = np.zeros(n, dtype=int)

        for label, c in enumerate(cluster):
            for point in c:
                idx = np.where(np.all(X == point, axis=1))[0][0]
                labels[idx] = label

        return labels




X = np.array([
    [1, 2],
    [2, 3],
    [3, 2],
    [8, 8],
    [9, 8]
])

model = AgglomerativeClustering(n_cluster=2)
print(model.fit_predict(X))

                        
            
                    
            
        
