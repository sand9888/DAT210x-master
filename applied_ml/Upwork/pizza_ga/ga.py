import pandas as pd

all_users1_data = 'C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Upwork/pizza_ga/csv/Analytics_all_users_part1_20170607.csv'
all_users2_data = 'C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Upwork/pizza_ga/csv/Analytics_all_users_part2_20170607.csv'
all_users1 = pd.read_csv(all_users1_data, names = ['id', 'sessions', 'sess_duration', 'bounce_rate', 'revenue', 'transactions', 'conv_rate'], skiprows=6, header=0, dtype={'id':str})
all_users2 = pd.read_csv(all_users2_data, names = ['id', 'sessions', 'sess_duration', 'bounce_rate', 'revenue', 'transactions', 'conv_rate'], skiprows=6, header=0, dtype={'id':str})
all_users = all_users1.append(all_users2)



# all_users = pd.read_csv('dataframe_main.csv')

common_name = ['returning_users', 'search_traffic', 'single_session_users', 'source_Google', 'source_MAILRU',
			   'source_VK', 'source_Yandex', 'users_bounced_sessions', 'users_desctop', 'users_direct_traffic',
			   'users_from_Gomel', 'users_mobile', 'users_organic_traffic', 'users_referral_traffic',
			   'users_sessions_more60sec', 'users_tablet']
for name in common_name:
	filename3 = 'C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Upwork/pizza_ga/csv/Analytics_' + name + '_20170607.csv'
	df_common_3 = pd.read_csv(filename3, names = ['id', 'sessions', 'sess_duration', 'bounce_rate', 'revenue', 'transactions', 'conv_rate'], skiprows=6, header=0, dtype={'id':str})
	df_common_3[name] = 1
	df_common_3 = df_common_3[['id', name]]
	all_users = pd.merge(all_users, df_common_3, how='left', on=['id'])

all_users['bounce_rate'] = all_users['bounce_rate'].str.replace('%','').astype(float)


all_users['sess_duration'] = pd.to_timedelta(all_users['sess_duration']).dt.total_seconds()
all_users.loc[(all_users['single_session_users'] == 0) & (all_users['returning_users'] == 1), 'label'] = 1
all_users.fillna(0, axis = 1, inplace=True)
all_users.to_csv('pizza_all_users.csv')
print(all_users)