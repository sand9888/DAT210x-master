import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing


df1 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWCustomers.csv', header=0)
df2 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWSales.csv', header=0)

# print(df1.head(), df2.head(5))

# df = df1.join(df2, on='CustomerID', how='left')
df = df1.merge(df2, how='left', left_on='CustomerID', right_on='CustomerID')
df.drop_duplicates(subset='CustomerID', inplace=True)
# df.dropna(axis=0, inplace=True)



data = df.drop(labels=['BikeBuyer', 'CustomerID', 'FirstName', 'MiddleName', 'LastName', 'PhoneNumber', 'LastUpdated',
					   'AddressLine2', 'Title', 'Suffix'], axis=1)
#print(data.head(30))
data.fillna(value=0, axis=0, inplace=True)
print(data[pd.isnull(data).any(axis=1)])
labels = df.BikeBuyer
labels = pd.get_dummies(labels)
# data.BirthDate = pd.to_datetime(data.BirthDate)
data = pd.get_dummies(data=data, columns=['AddressLine1', 'City', 'StateProvinceName', 'CountryRegionName', 'PostalCode', 'Education',
	  'Occupation', 'Gender', 'MaritalStatus', 'BirthDate'])
#data.Gender = pd.get_dummies(data.Gender)
#data.MaritalStatus = pd.get_dummies(data.MaritalStatus)
print(data.shape)
# splitting
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.4, random_state=7)

# normalization
T = preprocessing.Normalizer().fit(X_train)
X_train = T.transform(X_train)
X_test = T.transform(X_test)
#T = preprocessing.StandardScaler().fit_transform(df)
#T = preprocessing.MinMaxScaler().fit_transform(df)
#T = preprocessing.MaxAbsScaler().fit_transform(df)
#T = preprocessing.Normalizer().fit_transform(df)


# model
model = RandomForestClassifier(n_estimators=100, max_depth=20, min_samples_split=5, oob_score=True, random_state=0)

model.fit(X_train, y_train)
score = model.score(X_test, y_test)

score = model.oob_score_
print("OOB Score: ", round(score*100, 3))

score = model.score(X_test, y_test)
print("Score: ", round(score*100, 3))
