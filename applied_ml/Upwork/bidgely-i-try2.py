import pandas as pd
import numpy as np

filename = 'disagg.csv'
df_disagg = pd.read_csv(filename)
df_disagg.Month = pd.to_datetime(df_disagg.Month, yearfirst=True, format='%m/%d/%y %H:%M')

# leaving only month and year in 'Month' column
df_disagg['Month'] = df_disagg['Month'].apply(lambda x: str(x)[:7])
# df_disagg.Month = pd.to_datetime(df_disagg.Month)

df_raw = df_disagg[df_disagg.AppId == 0].reset_index()
df_non_raw = df_disagg[df_disagg.AppId != 0].reset_index()

def quantile_number(quant_number=5):

    df_final = pd.DataFrame()
    for i, dat in zip(list(df_raw.NhoodId.unique()), list(df_raw.Month.unique())):
        df_nhoodid = df_raw[df_raw.NhoodId == int(i)]
        df_nhoodid =  df_nhoodid[df_nhoodid.Month == dat]
        df_nhoodid['QuantileId'] = pd.qcut(df_nhoodid['Consumption'], quant_number, labels = [i for i in range(1, quant_number+1)])
        df_final = df_final.append(df_nhoodid)

        for date_month, quant, uuid in zip(df_final['Month'], df_final['QuantileId'], df_final['UUID']):
            df_non_raw.loc[(df_non_raw['Month'] == date_month) & (df_non_raw['UUID'] == uuid), 'QuantileId'] = quant
        # print(df_non_raw.head(10))
    df_final['Average'] = df_final.groupby(['NhoodId', 'Month', 'QuantileId', 'AppId'])['Consumption'].transform('mean')
    df_final['Median'] = df_final.groupby(['NhoodId', 'Month', 'QuantileId', 'AppId'])['Consumption'].transform('median')
    # df_final['Average'] = df_final['Consumption'].groupby(df_final['NhoodId', 'Month', 'QuantileId', 'AppId']).transform('mean')
    # df_final['Median'] = df_final['Consumption'].groupby(df_final['NhoodId', 'Month', 'QuantileId', 'AppId']).transform('median')
    print(df_final.head(10))
    '''quant_index = list(df_non_raw['QuantileId'].unique())
        for q_ind in quant_index:
            mean = df_non_raw.loc['QuantileId' == q_ind, 'Consumption'].mean()
            median = df_non_raw.loc['QuantileId' == q_ind, 'Consumption'].median()
            for date_month2, quant2, appid2 in zip(df_final['Month'], df_final['QuantileId'], df_final['AppId']):
                df_non_raw['Average'] = df_non_raw[(df_non_raw['Month'] == date_month2) & (df_non_raw['AppId'] == appid2) & (df_non_raw['QuantileId'] == q_ind)]['Consumption']/mean
                df_non_raw['Median'] = df_non_raw[(df_non_raw['Month'] == date_month2) & (df_non_raw['AppId'] == appid2) & (df_non_raw['QuantileId'] == q_ind)]['Consumption']/median'''

            
            
    return df_final, df_non_raw

df_final = quantile_number()
# print(df_non_raw)