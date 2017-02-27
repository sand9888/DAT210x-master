import numpy as np
from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)
print(pca.fit(X))
#pca.fit(df)
#pca.transform(df)

#print(pca.explained_variance_ratio_)
print(pca.components_)