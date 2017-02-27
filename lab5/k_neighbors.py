import pandas as pd
# From now on, you only train on a "portion" of your dset:
X_train = pd.DataFrame([ [0], [1], [2], [3] ])
y_train = [0, 0, 1, 1]

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
KNeighborsClassifier(...)

# You can pass in a dframe or an ndarray
model.predict([[1.1]])

model.predict_proba([[0.9]])
#[[ 0.66666667  0.33333333]]