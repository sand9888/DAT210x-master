# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to
import pandas as pd


df1 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWCustomers.csv', header=0)
df2 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWSales.csv', header=0)

# print(df1.head(), df2.head(5))

# df = df1.join(df2, on='CustomerID', how='left')
df = df1.merge(df2, how='left', left_on='CustomerID', right_on='CustomerID')
def azureml_main(df):
	df.BirthDate = df.BirthDate.astype('str')
	df['Age2'] = df['BirthDate'].apply(lambda x: 2017 - int(x[0:4]))
	# df.ix[df.Age2 > 59, 'Age2'] = df.Age2.median()
	df.BirthDate = pd.to_datetime(df.BirthDate)
	df.BirthDate = df.BirthDate.dt.year
	
	df.drop(df[df.Age2 > 56].index, axis=0, inplace=True)
	df.drop(df[df.BirthDate < 1963].index, axis=0, inplace=True)
	
	age = []
	# For each row in the column,
	for i in df['BirthDate']:
		# if more than a value,
		if i > 1986:
			# Append a letter grade
			age.append('<30years')
		# else, if more than a value,
		elif i <= 1986:
			# Append a letter grade
			age.append('>30years')
	
	df['Age'] = age
	
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
		if a == 'M' and b == '>30years' and c > 90000:
			rich_man.append(1)
		else:
			rich_man.append(0)
	print(rich_man)
	df['Richman'] = rich_man
	
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
	
	income = []
	# For each row in the column,
	for i in df['YearlyIncome']:
		# if more than a value,
		if i <= 35000:
			# Append a letter grade
			income.append('<35k')
		# else, if more than a value,
		elif i > 35000 and i <= 60000:
			# Append a letter grade
			income.append('30-60k')
		elif i > 60000 and i <= 90000:
			# Append a letter grade
			income.append('60-90k')
		elif i > 90000:
			# Append a letter grade
			income.append('>90k')
	
	df['Income'] = income
	
	# df.ix[df.NumberCarsOwned > 3, 'NumberCarsOwned'] = df.NumberCarsOwned.median()
	# df.ix[df.BirthDate < 1951, 'BirthDate'] = df.BirthDate.median()
	
	return df

azureml_main(df)