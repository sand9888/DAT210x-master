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


def quantile_number(quant_number=5, min_est_level = 10000):
    df_final = pd.DataFrame()
    for i in list(df_raw.NhoodId.unique()):
        for dat in list(df_raw.Month.unique()):
            df_nhoodid = df_raw[df_raw.NhoodId == int(i)]
            df_nhoodid = df_nhoodid[df_nhoodid.Month == dat]
            df_nhoodid['QuantileId'] = pd.qcut(df_nhoodid['Consumption'], quant_number, labels=[i for i in range(1, quant_number + 1)])
            df_final = df_final.append(df_nhoodid)
    
    # replacing for-loop with join:
    df_final2 = df_final[['UUID', 'Month', 'QuantileId']]
    for id in list(df_final['QuantileId'].unique()):
        # variant1
        # df1 = df_final[(df_final['QuantileId'] == id)].join(df_non_raw[(df_non_raw['Month'] == df_final['Month']) & (df_non_raw['UUID'] == df_final['UUID'])])
        # variant2
        # result = pd.merge(df_final[(df_final['QuantileId'] == id)], df_non_raw[(df_non_raw['Month'] == df_final['Month']) & (df_non_raw['UUID'] == df_final['UUID'])], on='UUID')
        # variant3

        df_non_raw2 = pd.merge(df_final2[(df_final2['QuantileId'] == id)], df_non_raw, on=['UUID', 'Month'], how='inner')
        df_non_raw2['QuantileId'] = id
        
        # variant4
        #df_non_raw['QuantileId'] = df_final['QuantileId'].applymap(lambda x: x['QuantileId'] if x['Month'] == df_non_raw['Month'] & x['UUID'] == df_non_raw['UUID'] else 'Nan', axis=0)
    
    # for date_month, quant, uuid in zip(df_final['Month'], df_final['QuantileId'], df_final['UUID']):
    #	df_non_raw.loc[(df_non_raw['Month'] == date_month) & (df_non_raw['UUID'] == uuid), 'QuantileId'] = quant
    # print(df_non_raw.head(10))
    
    # calculating Average, Median
    df_final['Average'] = df_final.groupby(['NhoodId', 'Month', 'QuantileId', 'AppId'])['Consumption'].transform('mean')
    df_final['Median'] = df_final.groupby(['NhoodId', 'Month', 'QuantileId', 'AppId'])['Consumption'].transform(
        'median')

    # calculating Average%, Median%
    list_quant = list(df_non_raw2['QuantileId'].unique())
    # list_quant.remove('nan')
    list_quant = [x for x in list_quant if str(x) != 'nan']
    for ii in list_quant:
        df_final['Average%'] = df_final['Average'] / df_non_raw2.loc[
            (df_non_raw2['QuantileId'] == ii) & (df_final['QuantileId'] == ii), 'Consumption'].mean()
        df_final['Median%'] = df_final['Average'] / df_non_raw2.loc[
            (df_non_raw2['QuantileId'] == ii) & (df_final['QuantileId'] == ii), 'Consumption'].median()
    df_final['Average-error'] = df_final['Average'] - df_final['Consumption']
    df_final['Average-error%'] = (df_final['Average'] - df_final['Consumption']) / df_final['Consumption']


    #df_final['Average'].hist(by=df_final['AppId'])
    #df_final['Average'].hist(by=df_final['Month'])
    #df_final['Average'].hist(by=df_final['NhoodId'])
    #plt.show()

    #detection
    df_final.loc[(df_final['Consumption'] > min_est_level) & (df_final['Average'] > min_est_level), 'Detection'] = 'TP'
    df_final.loc[(df_final['Consumption'] < min_est_level) & (df_final['Average'] > min_est_level), 'Detection'] = 'FP'
    df_final.loc[(df_final['Consumption'] > min_est_level) & (df_final['Average'] < min_est_level), 'Detection'] = 'FN'
    df_final.loc[(df_final['Consumption'] < min_est_level) & (df_final['Average'] < min_est_level), 'Detection'] = 'TN'


    df_sum_month = pd.DataFrame()
    df_final['Month'] = df_final['Month'].apply(lambda x: str(x)[5:7])
    list_month = list(df_final['Month'].unique())
    df_sum_month['Month'] = list_month

    list_tp = []
    for iii in list_month:
        list_tp.append(df_final.loc[(df_final.Month == iii) & (df_final.Detection == 'TP'), 'Detection'].count())
    df_sum_month['TP'] = list_tp
    list_tn = []
    for iii in list_month:
        list_tn.append(df_final.loc[(df_final.Month == iii) & (df_final.Detection == 'TN'), 'Detection'].count())
    df_sum_month['TN'] = list_tn
    list_fp = []
    for iii in list_month:
        list_fp.append(df_final.loc[(df_final.Month == iii) & (df_final.Detection == 'FP'), 'Detection'].count())
    df_sum_month['FP'] = list_fp
    list_fn = []
    for iii in list_month:
        list_fn.append(df_final.loc[(df_final.Month == iii) & (df_final.Detection == 'FN'), 'Detection'].count())
    df_sum_month['FN'] = list_fn
    df_sum_month['Precision'] = df_sum_month['TP'] / (df_sum_month['TP'] +  df_sum_month['FP'])
    df_sum_month['Recall'] = df_sum_month['TP'] / (df_sum_month['TP'] + df_sum_month['FN'])

    df_sum_month = df_sum_month.sort_values(by='Month').reset_index()
    print(df_sum_month)
    return df_final, df_non_raw

df_final = quantile_number()