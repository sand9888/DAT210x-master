import pandas as pd
import numpy as np
import os

# reading dataset
root_dir = os.path.abspath('../Upwork')
filename = 'disagg.csv'
df_scource = pd.read_csv(os.path.join(root_dir, filename))
df_scource.Month = pd.to_datetime(df_scource.Month, yearfirst=True, format='%m/%d/%y %H:%M')
df_scource['Month'] = df_scource['Month'].apply(lambda x: str(x)[:7])
# print(df.Month.dt.year)

# remain data where AppId equals 0
df = df_scource[df_scource['AppId'] == 0].reset_index()
df_non_raw = df_scource[df_scource.AppId != 0].reset_index()
df_non_raw['quantileId'] = np.nan


# dividing data by percentiles as function parameter
def quantile_number(quant_num=5):
	# creating empty dataframe
	df_final = pd.DataFrame()
	for i in list(df.NhoodId.unique()):
		df_id = df[df.NhoodId == int(i)]
		
		# calculate quantiles values
		quant_val = 100 / quant_num
		for i in range(1, quant_num + 1):
			if i == 1:
				df_q = df_id[df_id.Consumption <= np.percentile(df.Consumption, quant_val * i)]
				df_q.loc[:, 'quantileId'] = i
				df_final = df_final.append(df_q)
			
			else:
				df_q = df_id[(df_id.Consumption > np.percentile(df.Consumption, quant_val * (i - 1))) & (
				df_id.Consumption <= np.percentile(df.Consumption, quant_val * i))]
				df_q.loc[:, 'quantileId'] = i
				df_final = df_final.append(df_q)
	
	
	
	for i in range(1, quant_num + 1):
		quant = df_final[df_final.quantileId == i]
		print('Quantile ', i, ': \n', 'Average Consumption:', quant['Consumption'].mean(), '\n', 'Median Consumption: ',
			  quant['Consumption'].median())
	df_final['Consumption_mean_percent'] = df_final['Consumption'] / df_non_raw['Consumption'].mean()
	df_final['Consumption_median_percent'] = df_final['Consumption'] / df_non_raw['Consumption'].median()
	return df_final


df_final = quantile_number()

