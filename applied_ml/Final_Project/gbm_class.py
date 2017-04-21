import pandas as pd
from sklearn import model_selection
from sklearn import preprocessing
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier  #GBM algorithm
from sklearn import cross_validation, metrics   #Additional scklearn functions
from sklearn.model_selection import GridSearchCV   #Perforing grid search


import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4

df1 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWCustomers.csv', header=0)
df2 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWSales.csv', header=0)

# print(df1.head(), df2.head(5))

# df = df1.join(df2, on='CustomerID', how='left')
df = df1.merge(df2, how='left', left_on='CustomerID', right_on='CustomerID')
df.drop_duplicates(subset='CustomerID', inplace=True)
df.BirthDate = pd.to_datetime(df.BirthDate)
df.BirthDate = df.BirthDate.dt.year

income = []
# For each row in the column,
for i in df['YearlyIncome']:
    # if more than a value,
    if i > 62000:
        # Append a letter grade
        income.append('>62k')
    # else, if more than a value,
    elif i <= 62000:
        # Append a letter grade
        income.append('<=62k')
    # else, if more than a value,
df['Income'] = income

age = []
# For each row in the column,
for i in df['BirthDate']:
    # if more than a value,
    if i > 1987:
        # Append a letter grade
        age.append('<30years')
    # else, if more than a value,
    elif i <= 1987 and i >= 1967:
    # Append a letter grade
        age.append('30-50years')
    # else, if more than a value,
    elif i <= 1967:
    # Append a letter grade
        age.append('>50years')
df['Age'] = age

df.ix[df.NumberCarsOwned > 3, 'NumberCarsOwned'] = df.NumberCarsOwned.median()

df = df.drop(labels=['FirstName', 'MiddleName', 'LastName', 'PhoneNumber', 'LastUpdated',
                      'AddressLine2', 'AddressLine1', 'Title', 'Suffix', 'City', 'StateProvinceName',
	'CountryRegionName', 'PostalCode', 'CustomerID', 'HomeOwnerFlag', 'AvgMonthSpend' , 'BirthDate', 'TotalChildren'], axis=1)

df.fillna(value=0, axis=0, inplace=True)

# print(df.apply(lambda x: sum(x.isnull())))
labels = df.BikeBuyer
#labels = pd.get_dummies(labels)
# data.BirthDate = pd.to_datetime(data.BirthDate)
train = pd.get_dummies(data=df, columns=['Education', 'Occupation', 'Gender', 'MaritalStatus', 'Income',
									'Age', 'NumberChildrenAtHome', 'NumberCarsOwned', 'YearlyIncome'])
print(df.dtypes)
#print(train[pd.isnull(train).any(axis=1)])
#train = df
target = labels
IDcol = 'CustomerID'


def modelfit(alg, dtrain, predictors, performCV=True, printFeatureImportance=True, cv_folds=5):
	# Fit the algorithm on the data
	alg.fit(dtrain[predictors], dtrain['BikeBuyer'])
	
	
	# Predict training set:
	dtrain_predictions = alg.predict(dtrain[predictors])
	
	dtrain_predprob = alg.predict_proba(dtrain[predictors])[:, 1]
	
	
	# Perform cross-validation:
	if performCV:
		cv_score = model_selection.cross_val_score(alg, dtrain[predictors], dtrain['BikeBuyer'], cv=cv_folds,
													scoring='roc_auc')
	
	# Print model report:
	print("\nModel Report")
	print("Accuracy : %.4g") % metrics.accuracy_score(dtrain['BikeBuyer'], dtrain_predictions)
	print("AUC Score (Train): %f") % metrics.roc_auc_score(dtrain['BikeBuyer'], dtrain_predprob)
	
	if performCV:
		print("CV Score : Mean - %.7g | Std - %.7g | Min - %.7g | Max - %.7g") % (
		np.mean(cv_score), np.std(cv_score), np.min(cv_score), np.max(cv_score))
	
	# Print Feature Importance:
	if printFeatureImportance:
		feat_imp = pd.Series(alg.feature_importances_, predictors).sort_values(ascending=False)
		feat_imp.plot(kind='bar', title='Feature Importances')
		plt.ylabel('Feature Importance Score')
		plt.show()


#Choose all predictors except target & IDcols
train_col = train.drop(labels=['BikeBuyer'], axis=1)
predictors = [x for x in train_col.columns]
gbm0 = GradientBoostingClassifier(random_state=10)
modelfit(gbm0, train, predictors)