import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df1 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWCustomers.csv', header=0)
df2 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWSales.csv', header=0)

#print(df1.head(), df2.head(5))

#df = df1.join(df2, on='CustomerID', how='left')
df = df1.merge(df2, how='left', left_on='CustomerID', right_on='CustomerID')
df.drop_duplicates(subset='CustomerID', inplace=True)
#df.dropna(axis=0, inplace=True)
#print(df.head(5), df.shape)



df['Age2'] = df['BirthDate'].apply(lambda x: 2017 - int(x[0:4]))
df.drop(df[df.Age2 > 65].index, axis = 0, inplace = True)

df.drop(df[df.AvgMonthSpend > 63].index, axis = 0, inplace = True)
df.ix[df.Age2 > 70, 'Age2'] = df.Age2.median()
df.BirthDate = pd.to_datetime(df.BirthDate)
df.BirthDate = df.BirthDate.dt.year
df.drop(df[df.BirthDate < 1952].index, axis = 0, inplace = True)


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
	elif i > 60000 and i <= 90000:
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
	if i >= 1992:
		# Append a letter grade
		age.append('<25years')
	# else, if more than a value,
	elif i < 1992 and i >= 1982:
		# Append a letter grade
		age.append('25-35years')
	# else, if more than a value,
	elif i < 1982 and i >= 1972:
		# Append a letter grade
		age.append('35-45years')
	elif i < 1972 and i >= 1962:
		# Append a letter grade
		age.append('45-55years')
	elif i < 1962:
		# Append a letter grade
		age.append('>55years')
df['Age'] = age

mid_age_cr = []
for i, ii in zip(df['BirthDate'], df['Gender']):
	# if more than a value,
	if i > 1968 and i <= 1982 and ii == 'M':
		
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
	elif i == 1:
		car_owner.append(1)
	elif i >= 2:
		car_owner.append(2)
df['CarOwner'] = car_owner

children_at_home = []
for i in df.NumberChildrenAtHome:
	if i == 0:
		children_at_home.append(0)
	else:
		children_at_home.append(1)
df['ChildrenHome'] = children_at_home


def cond_hists(df, plot_cols, grid_col):
	import matplotlib.pyplot as plt
	## Loop over the list of columns
	for col in plot_cols:
		grid1 = sns.FacetGrid(df, col=grid_col)
		grid1.map(plt.hist, col, alpha=.7)
		grid1.map(vertical_median_line, col)
		plt.show()
	return grid_col

def vertical_median_line(x, **kwargs):
    plt.axvline(x.median(), **kwargs)
## Define columns for making a conditioned histogram
plot_cols2 = ['AvgMonthSpend']

cond_hists(df, plot_cols2, 'Age')



'''
def whiskey(df):
	import matplotlib
	matplotlib.use('agg')  # Set backend
	import numpy as np
	import matplotlib.pyplot as plt
	
	## Now make some box plots of the columbns with numerical values.
	names = df.columns.tolist()
	for col in names:
		if (df[col].dtype in [np.int64, np.int32, np.float64]):
			temp1 = df.ix[df.MaritalStatus == 'S', col]
			temp0 = df.ix[df.MaritalStatus == 'M', col]
			
			fig = plt.figure(figsize=(12, 6))
			fig.clf()
			ax1 = fig.add_subplot(1, 2, 1)
			ax0 = fig.add_subplot(1, 2, 2)
			ax1.boxplot(temp1.as_matrix())
			ax1.set_title('Box plot of ' + col + '\n for single')
			ax0.boxplot(temp0.as_matrix())
			ax0.set_title('Box plot of ' + col + '\n for married')

			plt.show()
	
	return ('Done')
whiskey(df)
'''


import matplotlib
matplotlib.use('agg')  # Set backend

df.plot.scatter(x='AvgMonthSpend', y='YearlyIncome')

df.plot.scatter(x='AvgMonthSpend', y='BirthDate')
df.plot.scatter(x='AvgMonthSpend', y='Age2')
df.plot.scatter(x='BikeBuyer', y='AvgMonthSpend')

plt.show()

'''
fig, axes = plt.subplots(nrows=2, sharex=True)
y = df[df['MaritalStatus'=='M'], df]
print(y)
axes[0].plot(df['AvgMonthSpend'], y, 'bo')
axes[1].plot(df['AvgMonthSpend'], y, 'bo')

plt.show()'''


## Now make some box plots of the columbns with numerical values.
col = 'AvgMonthSpend'


temp1 = df.ix[(df.Income == '<30k'), col]
temp0 = df.ix[(df.Income == '>120k'), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for yearly income <30k ')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for yearly income >120k')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()

temp1 = df.ix[df.MaritalStatus == 'S', col]
temp0 = df.ix[df.MaritalStatus == 'M', col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for single')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for married')
ax1.set_autoscaley_on(False)
ax1.set_ylim([43,66])
ax0.set_autoscaley_on(False)
ax0.set_ylim([43,66])
plt.show()


temp1 = df.ix[df.NumberCarsOwned == 0, col]
temp0 = df.ix[df.NumberCarsOwned >= 1, col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for no car')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for 2 or more car')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()



temp1 = df.ix[df.Gender == 'M', col]
temp0 = df.ix[df.Gender == 'F', col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for  male')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for female')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()



temp1 = df.ix[df.NumberChildrenAtHome == 0, col]
temp0 = df.ix[df.NumberChildrenAtHome >= 1, col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for no children at home')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for 2 or more children at home')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()

temp1 = df.ix[df.TotalChildren <= 2, col]
temp0 = df.ix[df.TotalChildren > 2, col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for no children total')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for 2 or more children total')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()

temp1 = df.ix[df.CountryRegionName == 'United States', col]
temp0 = df.ix[df.CountryRegionName != 'United States', col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for USA')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for not USA')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()


temp1 = df.ix[df.HomeOwnerFlag == 0, col]
temp0 = df.ix[df.HomeOwnerFlag == 1, col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for HomeOwnerFlag')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for not HomeOwnerFlag')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()



temp1 = df.ix[(df.Gender == 'F') & (df.MaritalStatus == 'M'), col]
temp0 = df.ix[(df.Gender == 'F') & (df.MaritalStatus == 'S'), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for married female')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for single female')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()

temp1 = df.ix[(df.Gender == 'M') & (df.Age == '35-45years') & (df.YearlyIncome > 120000), col]
temp0 = df.ix[(df.Gender == 'M') & (df.Age == '35-45years') & (df.YearlyIncome < 120000), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for married female')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for single female')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()

temp1 = df.ix[(df.MidAgeCr == 1), col]
temp0 = df.ix[(df.MidAgeCr == 0), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for midagecr')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for not midagecr')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()

temp1 = df.ix[(df.Occupation == 'Management') | (df.Occupation == 'Professional'), col]
temp0 = df.ix[(df.Occupation != 'Management') & (df.Occupation != 'Professional'), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for professional')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for not professional')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()


temp1 = df.ix[(df.Occupation == 'Manual') | (df.Occupation == 'Skilled Manual'), col]
temp0 = df.ix[(df.Occupation != 'Manual') & (df.Occupation != 'Skilled Manual'), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for manual ')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for not manual')
ax1.set_autoscaley_on(False)
ax1.set_ylim([40,70])
ax0.set_autoscaley_on(False)
ax0.set_ylim([40,70])
plt.show()

