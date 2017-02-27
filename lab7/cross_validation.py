from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# Test how well your model can recall its training data:
model.fit(X_train, y_train).score(X_train, y_train)
#0.943262278808

# Test how well your model can predict unseen data:
model.fit(X_train, y_train).score(X_test, y_test)
#0.894716422024

# 10-Fold Cross Validation on your training data
from sklearn.model_selection import cross_val_score as cval
cval.cross_val_score(model, X_train, y_train, cv=10)
#array([ 0.93513514,  0.99453552,  0.97237569,  0.98888889,  0.96089385,
#        0.98882682,  0.99441341,  0.98876404,  0.97175141,  0.96590909])

cval.cross_val_score(model, X_train, y_train, cv=10).mean()
#0.97614938602520218