import numpy as np
from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
print(X)
pca = PCA(n_components=1)
print(pca.fit(X))
#pca.fit(df)
#pca.transform(df)

print(pca.explained_variance_)
print(pca.components_)