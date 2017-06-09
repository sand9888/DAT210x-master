import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'disagg-updated.csv'
df_disagg = pd.read_csv(filename)
df_disagg.Month = pd.to_datetime(df_disagg.Month, yearfirst=True, format='%m/%d/%y %H:%M')

# leaving only month and year in 'Month' column
df_disagg['Month'] = df_disagg['Month'].apply(lambda x: str(x)[:7])
# df_disagg.Month = pd.to_datetime(df_disagg.Month)

df_raw = df_disagg[df_disagg.AppId == 0].reset_index()
df_non_raw = df_disagg[df_disagg.AppId != 0].reset_index()


def quantile_number(quant_number=5, min_est_level=10000):
	df_final = pd.DataFrame()
	for i in list(df_raw.NhoodId.unique()):
		for dat in list(df_raw.Month.unique()):
			df_nhoodid = df_raw[df_raw.NhoodId == int(i)]
			df_nhoodid = df_nhoodid[df_nhoodid.Month == dat]
			df_nhoodid['QuantileId'] = pd.qcut(df_nhoodid['Consumption'], quant_number,
											   labels=[i for i in range(1, quant_number + 1)])
			df_final = df_final.append(df_nhoodid)
	
	# replacing for-loop with join:
	df_final2 = df_final[['UUID', 'Month', 'QuantileId']]
	df_non_raw3 = pd.DataFrame()
	for id in list(df_final['QuantileId'].unique()):
		df_final2 = df_final[['UUID', 'Month', 'QuantileId']]
		df_non_raw2 = pd.merge(df_final2[(df_final2['QuantileId'] == id)], df_non_raw, on=['UUID', 'Month'],
							   how='inner')
		df_non_raw2['QuantileId'] = id
		df_non_raw3 = df_non_raw3.append(df_non_raw2, ignore_index=True)
	
	df_non_raw3 = df_non_raw3[['index', 'NhoodId', 'UUID', 'AppId', 'Month', 'Consumption', 'QuantileId']]
	
	df_final['Raw'] = df_final['Consumption']
	
	df1 = df_final[['UUID', 'Month', 'Raw']]
	df2 = df_non_raw3[['UUID', 'Month']]
	df3 = df2.merge(df1)
	df_non_raw3['Raw'] = df3['Raw']
	df_final = df_final.append(df_non_raw3, ignore_index=True)
	print(df_final)
	
	# calculating Average, Median
	df_final['Average'] = df_final.groupby(['NhoodId', 'Month', 'QuantileId', 'AppId'])['Consumption'].transform('mean')
	df_final['Median'] = df_final.groupby(['NhoodId', 'Month', 'QuantileId', 'AppId'])['Consumption'].transform(
		'median')
	
	# calculating Average%, Median%
	list_quant = list(df_non_raw3['QuantileId'].unique())
	# list_quant.remove('nan')
	list_quant = [x for x in list_quant if str(x) != 'nan']
	for ii in list_quant:
		df_final['Average%'] = df_final['Average'] / df_final.loc[
			df_final['QuantileId'] == ii, 'Consumption'].mean()
		df_final['Median%'] = df_final['Average'] / df_final.loc[
			df_final['QuantileId'] == ii, 'Consumption'].median()
	df_final['Average-error'] = df_final['Average'] - df_final['Consumption']
	df_final['Average-error%'] = (df_final['Average'] - df_final['Consumption']) / df_final['Consumption']
	df_final['Average-error(% of raw)'] = (df_final['Average'] - df_final['Consumption']) / df_final['Raw']
	
	# df_final['Average'].hist(by=df_final['AppId'])
	# df_final['Average'].hist(by=df_final['Month'])
	# df_final['Average'].hist(by=df_final['NhoodId'])
	# plt.show()
	
	# detection
	df_final.loc[(df_final['Consumption'] > min_est_level) & (df_final['Average'] > min_est_level), 'Detection'] = 'TP'
	df_final.loc[(df_final['Consumption'] < min_est_level) & (df_final['Average'] > min_est_level), 'Detection'] = 'FP'
	df_final.loc[(df_final['Consumption'] > min_est_level) & (df_final['Average'] < min_est_level), 'Detection'] = 'FN'
	df_final.loc[(df_final['Consumption'] < min_est_level) & (df_final['Average'] < min_est_level), 'Detection'] = 'TN'
	
	df_sum_month = pd.DataFrame()
	df_final['Month'] = df_final['Month'].apply(lambda x: str(x)[5:7])
	list_month = list(df_final['Month'].unique())
	df_sum_month['Month'] = list_month
	
	df_final_heating = df_final[df_final['AppId'] == 3]
	df_final_cooling = df_final[df_final['AppId'] == 4]
	
	# heating
	list_tp_heating = []
	list_tn_heating = []
	list_fp_heating = []
	list_fn_heating = []
	# cooling
	list_tp_cooling = []
	list_tn_cooling = []
	list_fp_cooling = []
	list_fn_cooling = []
	
	for iii in list_month:
		# heating
		list_tp_heating.append(df_final_heating.loc[(df_final_heating.Month == iii) & (
		df_final_heating.Detection == 'TP'), 'Detection'].count())
		list_tn_heating.append(df_final_heating.loc[(df_final_heating.Month == iii) & (
		df_final_heating.Detection == 'TN'), 'Detection'].count())
		list_fp_heating.append(df_final_heating.loc[(df_final_heating.Month == iii) & (
		df_final_heating.Detection == 'FP'), 'Detection'].count())
		list_fn_heating.append(df_final_heating.loc[(df_final_heating.Month == iii) & (
		df_final_heating.Detection == 'FN'), 'Detection'].count())
		# cooling
		list_tp_cooling.append(df_final_cooling.loc[(df_final_cooling.Month == iii) & (
		df_final_cooling.Detection == 'TP'), 'Detection'].count())
		list_tn_cooling.append(df_final_cooling.loc[(df_final_cooling.Month == iii) & (
		df_final_cooling.Detection == 'TN'), 'Detection'].count())
		list_fp_cooling.append(df_final_cooling.loc[(df_final_cooling.Month == iii) & (
		df_final_cooling.Detection == 'FP'), 'Detection'].count())
		list_fn_cooling.append(df_final_cooling.loc[(df_final_cooling.Month == iii) & (
		df_final_cooling.Detection == 'FN'), 'Detection'].count())
	
	# heating confusion matrix
	df_sum_month['TP_heating'] = list_tp_heating
	df_sum_month['TN_heating'] = list_tn_heating
	df_sum_month['FP_heating'] = list_fp_heating
	df_sum_month['FN_heating'] = list_fn_heating
	df_sum_month['Precision_heating'] = df_sum_month['TP_heating'] / (
	df_sum_month['TP_heating'] + df_sum_month['FP_heating'])
	df_sum_month['Recall_heating'] = df_sum_month['TP_heating'] / (
	df_sum_month['TP_heating'] + df_sum_month['FN_heating'])
	
	# cooling confusion matrix
	df_sum_month['TP_cooling'] = list_tp_cooling
	df_sum_month['TN_cooling'] = list_tn_cooling
	df_sum_month['FP_cooling'] = list_fp_cooling
	df_sum_month['FN_cooling'] = list_fn_cooling
	df_sum_month['Precision_cooling'] = df_sum_month['TP_cooling'] / (
	df_sum_month['TP_cooling'] + df_sum_month['FP_cooling'])
	df_sum_month['Recall_cooling'] = df_sum_month['TP_cooling'] / (
	df_sum_month['TP_cooling'] + df_sum_month['FN_cooling'])
	
	# estimation% heating
	df_sum_month['Estimation %'] = df_sum_month['Month']
	
	# print(df_final)
	list_med_heating = []
	list_mean_heating = []
	list_20_heating = []
	list_80_heating = []
	list_med_cooling = []
	list_mean_cooling = []
	list_20_cooling = []
	list_80_cooling = []
	for iii in list_month:
		# heating
		list_med_heating.append(df_final_heating.loc[df_final_heating['Month'] == iii, 'Average-error%'].median())
		list_mean_heating.append(df_final_heating.loc[df_final_heating['Month'] == iii, 'Average-error%'].mean())
		list_20_heating.append(df_final_heating.loc[df_final_heating['Month'] == iii, 'Average-error%'].quantile(q=0.2))
		list_80_heating.append(df_final_heating.loc[df_final_heating['Month'] == iii, 'Average-error%'].quantile(q=0.8))
		# cooling
		list_med_cooling.append(df_final_cooling.loc[df_final_cooling['Month'] == iii, 'Average-error%'].median())
		list_mean_cooling.append(df_final_cooling.loc[df_final_cooling['Month'] == iii, 'Average-error%'].mean())
		list_20_cooling.append(df_final_cooling.loc[df_final_cooling['Month'] == iii, 'Average-error%'].quantile(q=0.2))
		list_80_cooling.append(df_final_cooling.loc[df_final_cooling['Month'] == iii, 'Average-error%'].quantile(q=0.8))
	# heating
	df_sum_month['Median_heating'] = list_med_heating
	df_sum_month['Mean_heating'] = list_mean_heating
	df_sum_month['20_percentile_heating'] = list_20_heating
	df_sum_month['80_percentile_heating'] = list_80_heating
	# cooling
	df_sum_month['Median_cooling'] = list_med_cooling
	df_sum_month['Mean_cooling'] = list_mean_cooling
	df_sum_month['20_percentile_cooling'] = list_20_cooling
	df_sum_month['80_percentile_cooling'] = list_80_cooling
	
	df_sum_month['Estimation (% of raw)'] = df_sum_month['Month']
	list_med_heating2 = []
	list_mean_heating2 = []
	list_20_heating2 = []
	list_80_heating2 = []
	list_med_cooling2 = []
	list_mean_cooling2 = []
	list_20_cooling2 = []
	list_80_cooling2 = []
	for iii in list_month:
		# heating
		list_med_heating2.append(
			df_final_heating.loc[df_final_heating['Month'] == iii, 'Average-error(% of raw)'].median())
		list_mean_heating2.append(
			df_final_heating.loc[df_final_heating['Month'] == iii, 'Average-error(% of raw)'].mean())
		list_20_heating2.append(
			df_final_heating.loc[df_final_heating['Month'] == iii, 'Average-error(% of raw)'].quantile(q=0.2))
		list_80_heating2.append(
			df_final_heating.loc[df_final_heating['Month'] == iii, 'Average-error(% of raw)'].quantile(q=0.8))
		# cooling
		list_med_cooling2.append(
			df_final_cooling.loc[df_final_cooling['Month'] == iii, 'Average-error(% of raw)'].median())
		list_mean_cooling2.append(
			df_final_cooling.loc[df_final_cooling['Month'] == iii, 'Average-error(% of raw)'].mean())
		list_20_cooling2.append(
			df_final_cooling.loc[df_final_cooling['Month'] == iii, 'Average-error(% of raw)'].quantile(q=0.2))
		list_80_cooling2.append(
			df_final_cooling.loc[df_final_cooling['Month'] == iii, 'Average-error(% of raw)'].quantile(q=0.8))
	# heating
	df_sum_month['Median_heating2'] = list_med_heating2
	df_sum_month['Mean_heating2'] = list_mean_heating2
	df_sum_month['20_percentile_heating2'] = list_20_heating2
	df_sum_month['80_percentile_heating2'] = list_80_heating2
	# cooling
	df_sum_month['Median_cooling2'] = list_med_cooling2
	df_sum_month['Mean_cooling2'] = list_mean_cooling2
	df_sum_month['20_percentile_cooling2'] = list_20_cooling2
	df_sum_month['80_percentile_cooling2'] = list_80_cooling2
	
	df_sum_month = df_sum_month.sort_values(by='Month').reset_index()
	
	# summary by UUID ( estimate %)
	# cooling mean
	df_final_cooling_UUID_mean = df_final_cooling.groupby('UUID').mean()
	df_final_cooling_UUID_mean.reset_index(level=0, inplace=True)
	df_final_cooling_UUID_mean = df_final_cooling_UUID_mean[['UUID', 'Average-error%']]
	df_final_cooling_UUID_mean.columns = ['Estimation %', 'Mean_cooling']
	
	# cooling median
	df_final_cooling_UUID_median = df_final_cooling.groupby('UUID').median()
	df_final_cooling_UUID_median.reset_index(level=0, inplace=True)
	df_final_cooling_UUID_median = df_final_cooling_UUID_median[['UUID', 'Average-error%']]
	df_final_cooling_UUID_median.columns = ['Estimation %', 'Median_cooling']
	
	# heating mean
	df_final_heating_UUID_mean = df_final_heating.groupby('UUID').mean()
	df_final_heating_UUID_mean.reset_index(level=0, inplace=True)
	df_final_heating_UUID_mean = df_final_heating_UUID_mean[['UUID', 'Average-error%']]
	df_final_heating_UUID_mean.columns = ['Estimation %', 'Mean_heating']
	
	# heating median
	df_final_heating_UUID_median = df_final_heating.groupby('UUID').median()
	df_final_heating_UUID_median.reset_index(level=0, inplace=True)
	df_final_heating_UUID_median = df_final_heating_UUID_median[['UUID', 'Average-error%']]
	df_final_heating_UUID_median.columns = ['Estimation %', 'Median_heating']
	
	# joining mean&median
	df_final_cooling_UUID = pd.merge(df_final_cooling_UUID_median, df_final_cooling_UUID_mean, on='Estimation %')
	df_final_heating_UUID = pd.merge(df_final_heating_UUID_median, df_final_heating_UUID_mean, on='Estimation %')
	df_final_UUID = pd.merge(df_final_heating_UUID, df_final_cooling_UUID, on='Estimation %')
	
	df_sum_month = df_sum_month.append(df_final_UUID)
	
	# summary by UUID ( estimate (% of raw))
	# cooling mean
	df_final_cooling_UUID_mean2 = df_final_cooling.groupby('UUID').mean()
	df_final_cooling_UUID_mean2.reset_index(level=0, inplace=True)
	df_final_cooling_UUID_mean2 = df_final_cooling_UUID_mean2[['UUID', 'Average-error(% of raw)']]
	df_final_cooling_UUID_mean2.columns = ['Estimation (% of raw)', 'Mean_cooling2']
	
	# cooling median
	df_final_cooling_UUID_median2 = df_final_cooling.groupby('UUID').median()
	df_final_cooling_UUID_median2.reset_index(level=0, inplace=True)
	df_final_cooling_UUID_median2 = df_final_cooling_UUID_median2[['UUID', 'Average-error(% of raw)']]
	df_final_cooling_UUID_median2.columns = ['Estimation (% of raw)', 'Median_cooling2']
	
	# heating mean
	df_final_heating_UUID_mean2 = df_final_heating.groupby('UUID').mean()
	df_final_heating_UUID_mean2.reset_index(level=0, inplace=True)
	df_final_heating_UUID_mean2 = df_final_heating_UUID_mean2[['UUID', 'Average-error(% of raw)']]
	df_final_heating_UUID_mean2.columns = ['Estimation (% of raw)', 'Mean_heating2']
	
	# heating median
	df_final_heating_UUID_median2 = df_final_heating.groupby('UUID').median()
	df_final_heating_UUID_median2.reset_index(level=0, inplace=True)
	df_final_heating_UUID_median2 = df_final_heating_UUID_median2[['UUID', 'Average-error(% of raw)']]
	df_final_heating_UUID_median2.columns = ['Estimation (% of raw)', 'Median_heating2']
	
	# joining mean&median
	df_final_cooling_UUID2 = pd.merge(df_final_cooling_UUID_median2, df_final_cooling_UUID_mean2,
									  on='Estimation (% of raw)')
	df_final_heating_UUID2 = pd.merge(df_final_heating_UUID_median2, df_final_heating_UUID_mean2,
									  on='Estimation (% of raw)')
	df_final_UUID2 = pd.merge(df_final_heating_UUID2, df_final_cooling_UUID2, on='Estimation (% of raw)')
	
	# appendin
	
	df_sum_month = df_sum_month.append(df_final_UUID2)
	
	# reordering columns
	df_sum_month = df_sum_month[['Month', 'TP_heating', 'TN_heating', 'FP_heating', 'FN_heating', 'Precision_heating',
								 'Recall_heating', 'TP_cooling', 'TN_cooling', 'FP_cooling', 'FN_cooling',
								 'Precision_cooling',
								 'Recall_cooling', 'Estimation %', 'Median_heating', 'Mean_heating',
								 '20_percentile_heating', '80_percentile_heating',
								 'Median_cooling', 'Mean_cooling', '20_percentile_cooling', '80_percentile_cooling',
								 'Estimation (% of raw)', 'Median_heating2', 'Mean_heating2', '20_percentile_heating2',
								 '80_percentile_heating2',
								 'Median_cooling2', 'Mean_cooling2', '20_percentile_cooling2', '80_percentile_cooling2',
								 'index'
								 ]]
	
	# print(df_final_cooling_UUID_mean.shape, df_final_cooling_UUID_median.shape)
	# print(df_final_cooling_UUID)
	df_sum_month.to_csv('test.csv')
	
	'''
	df_sum_uuid = pd.DataFrame()
	list_uuid = list(df_final['UUID'].unique())
	df_sum_uuid['UUID'] = list_uuid
	list_tp = []
	list_tn = []
	list_fp = []
	list_fn = []
	for iii in list_uuid:
		list_tp.append(df_final.loc[(df_final.UUID == iii) & (df_final.Detection == 'TP'), 'Detection'].count())
		list_tn.append(df_final.loc[(df_final.UUID == iii) & (df_final.Detection == 'TN'), 'Detection'].count())
		list_fp.append(df_final.loc[(df_final.UUID == iii) & (df_final.Detection == 'FP'), 'Detection'].count())
		list_fn.append(df_final.loc[(df_final.UUID == iii) & (df_final.Detection == 'FN'), 'Detection'].count())
	df_sum_uuid['TP'] = list_tp
	df_sum_uuid['TN'] = list_tn
	df_sum_uuid['FP'] = list_fp
	df_sum_uuid['FN'] = list_fn
	df_sum_uuid['Precision'] = df_sum_uuid['TP'] / (df_sum_uuid['TP'] + df_sum_uuid['FP'])
	df_sum_uuid['Recall'] = df_sum_uuid['TP'] / (df_sum_uuid['TP'] + df_sum_uuid['FN'])
	print(df_sum_uuid)'''
	return df_final, df_non_raw


df_final = quantile_number()