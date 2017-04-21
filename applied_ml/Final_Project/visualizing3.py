import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df1 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWCustomers.csv', header=0)
df2 = pd.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Final_Project/AWSales.csv', header=0)

# print(df1.head(), df2.head(5))

# df = df1.join(df2, on='CustomerID', how='left')
df = df1.merge(df2, how='left', left_on='CustomerID', right_on='CustomerID')
df.drop_duplicates(subset='CustomerID', inplace=True)
# df.dropna(axis=0, inplace=True)
# print(df.head(5), df.shape)
df['BithDate'] = pd.to_datetime(df['BirthDate'], yearfirst=True, format='%Y-%m-%d')
date = df.BirthDate[df['BithDate'] > '1998']
# print(df.BirthDate.head())

def cond_hists(df, plot_cols, grid_col):
	import matplotlib.pyplot as plt
	## Loop over the list of columns
	for col in plot_cols:
		grid1 = sns.FacetGrid(df, col=grid_col)
		grid1.map(plt.hist, col, alpha=.7)
		plt.show()
	return grid_col


## Define columns for making a conditioned histogram
plot_cols2 = ["AvgMonthSpend"]
cond_hists(df, plot_cols2, 'CountryRegionName')


col = 'AvgMonthSpend'
temp1 = df.ix[df.MaritalStatus == 'S', col].value_counts()
temp0 = df.ix[df.MaritalStatus == 'M', col].value_counts()
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for buyers')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for not buyers')
plt.show()



col = 'AvgMonthSpend'
temp1 = df.ix[(df.Gender == 'M') & (df.BirthDate <= '1998') & (df.BirthDate >= '1992'), col]
temp0 = df.ix[(df.Gender == 'F') & (df.BirthDate <= '1998') & (df.BirthDate >= '1992'), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for younger male')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for younger female')

temp1 = df.ix[(df.Gender == 'M') & (df.BirthDate <= '1987') & (df.BirthDate >= '1967'), col]
temp0 = df.ix[(df.Gender == 'F') & (df.BirthDate <= '1987') & (df.BirthDate >= '1967'), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.boxplot(temp1.as_matrix())
ax1.set_title('Box plot of ' + col + '\n for older male')
ax0.boxplot(temp0.as_matrix())
ax0.set_title('Box plot of ' + col + '\n for older female')

plt.show()



