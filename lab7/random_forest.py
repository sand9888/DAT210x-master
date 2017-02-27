from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=10, oob_score=True)
model.fit(X, y)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
					   max_depth=None, max_features='auto', max_leaf_nodes=None,
					   min_samples_leaf=1, min_samples_split=2,
					   min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
					   oob_score=True, random_state=None, verbose=0, warm_start=False)


model.oob_score_
0.789925345