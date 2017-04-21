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

df.BirthDate = df.BirthDate.astype('str')

df['Age2'] = df['BirthDate'].apply(lambda x: 2017 - int(x[0:4]))
df.BirthDate = pd.to_datetime(df.BirthDate)
df.BirthDate = df.BirthDate.dt.year

def describe(df, col):
 ## Compute the summary stats
 desc = df[col].describe()

 ## Change the name of the 50% index to median
 idx = desc.index.tolist()
 idx[5] = 'median'
 desc.index = idx
 return print(desc)

describe(df, ['YearlyIncome', 'AvgMonthSpend', 'Age2', 'BirthDate'])
#print(df[['YearlyIncome', 'AvgMonthSpend', 'Age2']].describe())








income = []
# For each row in the column,
for i in df['YearlyIncome']:
    # if more than a value,
    if i <= 30000:
        # Append a letter grade
        income.append('<30k')
    # else, if more than a value,
    elif i > 30000 and i <= 60000:
        # Append a letter grade
        income.append('30-60k')
    elif i > 60000 and i <=90000:
        # Append a letter grade
        income.append('60-90k')
    elif i > 90000 and i <= 120000:
        # Append a letter grade
        income.append('90-120k')
    elif i > 120000:
        # Append a letter grade
        income.append('>120k')
    # else, if more than a value,
df['Income'] = income

age = []
# For each row in the column,
for i in df['BirthDate']:
    # if more than a value,
    if i > 1986:
        # Append a letter grade
        age.append('<30years')
    # else, if more than a value,
    # else, if more than a value,
    elif i <= 1986 and i >= 1967:
    # Append a letter grade
        age.append('30-50years')
    elif i < 1967:
    # Append a letter grade
        age.append('>50years')
df['Age'] = age

mid_age_cr = []
for i, ii in zip(df['BirthDate'], df['Gender']):
    # if more than a value,
    if i >= 1967 and i <= 1986 and ii == 'M':
       
        # Append a letter grade
        mid_age_cr.append(1)
    # else, if more than a value,
    else:
    # Append a letter grade
        mid_age_cr.append(0)
df['MidAgeCr'] = mid_age_cr

car_owner = []
for i in df.NumberCarsOwned:
	if i == 0:
		car_owner.append(0)
	else:
		car_owner.append(1)
df['CarOwner'] = car_owner

children_at_home = []
for i in df.NumberChildrenAtHome:
	if i == 0:
		children_at_home.append(0)
	else:
		children_at_home.append(1)
df['ChildrenHome'] = children_at_home

manual = []
for i in df.Occupation:
	if i == 'Manual' or i == 'Skilled Manual':
		manual.append(1)
	elif i != 'Manual' and i != 'Skilled Manual':
		manual.append(0)
df['Manual'] = manual

professional = []
for i in df.Occupation:
	if i == 'Professional' or i == 'Management':
		professional.append(1)
	elif i != 'Professional' and i != 'Management':
		professional.append(0)
df['Professional'] = professional

rich_man = []
for a, b, c in zip(df.Gender, df.Age, df.YearlyIncome):
	if a == 'M' and (b == '35-45years' or b == '45-55years' or b == '>55years') and c > 100000:
		rich_man.append(1)
	else:
		rich_man.append(0)
df['Richman'] = rich_man

car_owner = []
for i in df.NumberCarsOwned:
	if i == 0:
		car_owner.append(0)
	else:
		car_owner.append(1)
df['CarOwner'] = car_owner

df.ix[df.NumberCarsOwned > 3, 'NumberCarsOwned'] = df.NumberCarsOwned.median()
df44 = df[df.TotalChildren > 2]


'''

data = df.drop(labels=['BikeBuyer', 'CustomerID', 'FirstName', 'MiddleName', 'LastName', 'PhoneNumber', 'LastUpdated',
                       'AddressLine2', 'Title', 'Suffix'], axis=1)
#print(data.head(30))
#data.fillna(value=0, axis=0, inplace=True)
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
model = RandomForestClassifier(n_estimators=350, max_depth=50, min_samples_split=5, oob_score=True, random_state=0)

model.fit(X_train, y_train)
score = model.score(X_test, y_test)

score = model.oob_score_
print("OOB Score: ", round(score*100, 3))

score = model.score(X_test, y_test)
print("Score: ", round(score*100, 3))'''
