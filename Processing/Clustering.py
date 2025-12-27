import numpy as np

class KMeans:
    def __init__(self, gr, k, max_iter, tol):
        self.gr = gr
        self.k = k
        self.max_iter = max_iter
        self.tol = tol

    def clustering(self):
        # Initialize centroid starting positions (pick k values from the data)
        centroids = np.random.choice(self.gr, self.k, replace=False)

        for _ in range(self.max_iter):
            # 1) Compute distances
            distances = []
            for value in self.gr:
                row = []
                for c in centroids:
                    row.append(abs(value - c))
                distances.append(row)
            distances = np.array(distances)

            # 2) Assign labels: nearest centroid index for each value
            labels = np.argmin(distances, axis=1)

            # 3) Update centroids
            new_centroids = np.zeros(self.k)
            for i in range(self.k):
                cluster_points = self.gr[labels == i]
                if len(cluster_points) > 0:
                    new_centroids[i] = np.mean(cluster_points)
                else:
                    # Keep centroid if cluster is empty
                    new_centroids[i] = centroids[i]

            # 4) Check convergence
            change = np.max(np.abs(centroids - new_centroids))

            centroids = new_centroids

            if change < self.tol:
                break

        return labels, centroids
