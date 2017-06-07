import pandas as pd

df_common = pd.read_csv('20170531_common.csv', names = ['id', 'sessions', 'sess_duration', 'bounce_rate', 'revenue', 'transactions', 'conv_rate'], skiprows=6, header=0, dtype={'id':str})
# df_common.columns = []
#df_common.id = df_common.id.astype(str)

df_cpc = pd.read_csv('20170531_cpc.csv', names = ['id', 'sessions', 'sess_duration', 'bounce_rate', 'revenue', 'transactions', 'conv_rate'], skiprows=6, header=0, dtype={'id':str})
# df_cpc.columns = ['id', 'sessions', 'sess_duration', 'bounce_rate', 'revenue', 'transactions', 'conv_rate']
# df_cpc.id = df_cpc.id.astype(str)
df_cpc['cpc'] = 1
df_cpc = df_cpc[['id', 'cpc']]
# print(df_cpc, df_common)

# df_common = df_common.join(df_cpc, on='id', how='left')
df_common = pd.merge(df_common, df_cpc, how='left', on=['id'])
print(df_common.head(100))