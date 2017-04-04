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


def cond_hists(df, plot_cols, grid_col):
	import matplotlib.pyplot as plt
	## Loop over the list of columns
	for col in plot_cols:
		grid1 = sns.FacetGrid(df, col=grid_col)
		grid1.map(plt.hist, col, alpha=.7)
		plt.show()
	return grid_col


## Define columns for making a conditioned histogram
plot_cols2 = ["YearlyIncome",
			  "AvgMonthSpend"]

#cond_hists(df, plot_cols2, 'Occupation')

#num_cols = ["length", "curb-weight", "engine-size", "horsepower", "city-mpg", "compression-ratio", "fuel-type"]
#sns.pairplot(df[num_cols], size=3)


'''def whiskey(df):
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
			fig.savefig('box_' + col + '.png')
			plt.show()
	
	return ('Done')
whiskey(df)

'''

import matplotlib
matplotlib.use('agg')  # Set backend

## Now make some box plots of the columbns with numerical values.
col = 'AvgMonthSpend'
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


temp1 = df.ix[df.NumberCarsOwned == 0, col]
temp0 = df.ix[df.NumberCarsOwned >= 1, col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for no car')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for 1 or more car')
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
ax0.set_title('Box plot of ' + col + '\n for 1 or more children at home')
plt.show()









