from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
kmeans.fit(df)


labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_