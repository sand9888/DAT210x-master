import pandas as pd
import numpy as np
import os

# reading dataset
root_dir = os.path.abspath('../Upwork')
filename = 'disagg.csv'
df = pd.read_csv(os.path.join(root_dir, filename))

# remain data where AppId equals 0
df = df[df.AppId == 0]

df.sort_values(by=['NhoodId'], ascending=True, inplace=True)
df_final = pd.DataFrame()
for i in list(df.NhoodId.unique()):
	df_id = df[df.NhoodId == int(i)]
	
	df_1quant = df_id[df_id.Consumption <= np.percentile(df.Consumption,20)]
	df_1quant.loc[:,'quantileId'] = 1

	df_2quant = df_id[(df_id.Consumption > np.percentile(df.Consumption,20)) & (df_id.Consumption <= np.percentile(df.Consumption,40))]
	df_2quant.loc[:,'quantileId'] = 2

	df_3quant = df_id[(df_id.Consumption > np.percentile(df.Consumption,40)) & (df_id.Consumption <= np.percentile(df.Consumption,60))]
	df_3quant.loc[:,'quantileId'] = 3

	df_4quant = df_id[(df_id.Consumption > np.percentile(df.Consumption,60)) & (df_id.Consumption <= np.percentile(df.Consumption,80))]
	df_4quant.loc[:,'quantileId'] = 4

	df_5quant = df_id[df_id.Consumption > np.percentile(df.Consumption,80)]
	df_5quant.loc[:,'quantileId'] = 5

	df_new = pd.concat([df_1quant, df_2quant, df_3quant, df_4quant, df_5quant])
	df_final = df_final.append(df_new)

# computing descriptive statistic
for i in range(1,6):
	quant = df_final[df_final.quantileId == i]
	print('Quantile ', i, ': \n', 'Average Consumption:', quant['Consumption'].mean(), '\n', 'Median Consumption: ', quant['Consumption'].median())
