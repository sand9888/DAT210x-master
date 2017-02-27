from sklearn import linear_model
import numpy as np

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

# R2 Score
model.score(X_test, y_test)
153.244939109

# Sum of Squared Distances
np.sum(model.predict(X_test) - y_test) ** 2)
5465.15