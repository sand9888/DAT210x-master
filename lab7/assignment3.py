import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn import manifold

X = pd.read_csv('C:/DAT210x-master/Module6/Datasets/parkinsons.data')
X = X.drop(labels=['name'], axis=1)
y = X['status']
X = X.drop(labels=['status'], axis=1)
#print(X[pd.isnull(X).any(axis=1)])
#print(y.head(10))
#print(type(X), type(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)


T = preprocessing.StandardScaler().fit(X_train)
X_train = T.transform(X_train)
X_test = T.transform(X_test)
#T = preprocessing.MinMaxScaler().fit_transform(df)
#X_train =  preprocessing.MaxAbsScaler().fit_transform(X_train)
#preprocessing.Normalizer().fit_transform(X_train)
#preprocessing.KernelCenterer().fit_transform(X_train)

'''pca = PCA(n_components=4)
pca.fit(X_train)
X_train = pca.transform(X_train)
X_test = pca.transform(X_test)'''

iso = manifold.Isomap(n_neighbors=2, n_components=6)
iso.fit(X_train)
X_train = iso.transform(X_train)
X_test = iso.transform(X_test)




model = SVC()
model.fit(X_train, y_train)
print('N1',model.score(X_test, y_test))

test = []
best_score = 0
C_coef = 0
gamma_coef = 0
for cv in np.arange(0.05,2.0,0.05):
	for gamma in np.arange(0.001, 0.1, 0.001):
		model = SVC(C=cv, gamma=gamma)
		model.fit(X_train, y_train)
		current_score = model.score(X_test, y_test)
		test.append(current_score)
		#print(current_score)
		if current_score > best_score:
			best_score = current_score
			C_coef = cv
			gamma_coef = gamma
print(max(test))
print(best_score, C_coef, gamma_coef)
