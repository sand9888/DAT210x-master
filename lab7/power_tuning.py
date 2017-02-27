from sklearn import svm, grid_search, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

parameters = {'kernel':('linear', 'rbf'), 'C':[1, 5, 10]}
model = svm.SVC()

classifier = GridSearchCV(model, parameters)
classifier.fit(iris.data, iris.target)
#GridSearchCV(cv=None, error_score='raise',
#       estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#  max_iter=-1, probability=False, random_state=None, shrinking=True,
#  tol=0.001, verbose=False),
#       fit_params={}, iid=True, n_jobs=1,
#       param_grid={'kernel': ('linear', 'rbf'), 'C': [1, 5, 10]},
#       pre_dispatch='2*n_jobs', refit=True, scoring=None, verbose=0)


parameter_dist = {
  'C': scipy.stats.expon(scale=100),
  'kernel': ['linear'],
  'gamma': scipy.stats.expon(scale=.1),
}

classifier = RandomizedSearchCV(model, parameter_dist)
classifier.fit(iris.data, iris.target)

#RandomizedSearchCV(cv=None, error_score='raise',
#          estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#  max_iter=-1, probability=False, random_state=None, shrinking=True,
#  tol=0.001, verbose=False),
#          fit_params={}, iid=True, n_iter=10, n_jobs=1,
#          param_distributions={'kernel': ['linear'], 'C': <scipy.stats._distn_infrastructure.rv_frozen object at 0x110345c50>, 'gamma': <scipy.stats._distn_infrastructure.rv_frozen object at 0x110345d90>},
#          pre_dispatch='2*n_jobs', random_state=None, refit=True,
#          scoring=None, verbose=0)