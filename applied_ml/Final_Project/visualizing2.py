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
print(df.dtypes)


def bar(df):
	import matplotlib
	matplotlib.use('agg')  # Set backend
	import numpy as np
	import matplotlib.pyplot as plt
	
	## Create a series of bar plots for the various levels of the
	## string columns in the data frame by readmi_class.
	names = df.columns.tolist()
	for col in names:
		if (df[col].dtype not in [np.int64, np.int32, np.float64]):
			temp1 = df.ix[df.BikeBuyer == 1, col].value_counts()
			temp0 = df.ix[df.BikeBuyer == 0, col].value_counts()
			
			fig = plt.figure(figsize=(12, 6))
			fig.clf()
			ax1 = fig.add_subplot(1, 2, 1)
			ax0 = fig.add_subplot(1, 2, 2)
			temp1.plot(kind='bar', ax=ax1)
			ax1.set_title('Values of ' + col + '\n for buyers')
			temp0.plot(kind='bar', ax=ax0)
			ax0.set_title('Values of ' + col + '\n for not buyers')
			fig.savefig('bar_' + col + '.png')
	plt.show()
	return 'Done'


def box(df):
	import matplotlib
	matplotlib.use('agg')  # Set backend
	import numpy as np
	import matplotlib.pyplot as plt
	
	## Now make some box plots of the columbns with numerical values.
	names = df.columns.tolist()
	for col in names:
		if (df[col].dtype in [np.int64, np.int32, np.float64]):
			temp1 = df.ix[df.BikeBuyer == 1, col].value_counts()
			temp0 = df.ix[df.BikeBuyer == 0, col].value_counts()
			
			fig = plt.figure(figsize=(12, 6))
			fig.clf()
			ax1 = fig.add_subplot(1, 2, 1)
			ax0 = fig.add_subplot(1, 2, 2)
			ax1.boxplot(temp1.as_matrix())
			ax1.set_title('Box plot of ' + col + '\n for buyers')
			ax0.boxplot(temp0.as_matrix())
			ax0.set_title('Box plot of ' + col + '\n for not buyers')
			fig.savefig('box_' + col + '.png')
	plt.show()
	return 'Done'


def hist(df):
	import matplotlib
	matplotlib.use('agg')  # Set backend
	import numpy as np
	import matplotlib.pyplot as plt
	
	## Now make historgrams of the columbns with numerical values.
	names = df.columns.tolist()
	for col in names:
		if (df[col].dtype in [np.int64, np.int32, np.float64]):
			temp1 = df.ix[df.BikeBuyer == 1, col].value_counts()
			temp0 = df.ix[df.BikeBuyer == 0, col].value_counts()
			
			fig = plt.figure(figsize=(12, 6))
			fig.clf()
			ax1 = fig.add_subplot(1, 2, 1)
			ax0 = fig.add_subplot(1, 2, 2)
			ax1.hist(temp1.as_matrix(), bins=30)
			ax1.set_title('Histogram of ' + col + '\n for buyers')
			ax0.hist(temp0.as_matrix(), bins=30)
			ax0.set_title('Histogram of ' + col + '\n for not buyers')
			fig.savefig('hist_' + col + '.png')
	plt.show()
	return 'Done'


#hist(df)
bar(df)
#box(df)