from sklearn import manifold
iso = manifold.Isomap(n_neighbors=4, n_components=2)
iso.fit(df)
manifold = iso.transform(df)