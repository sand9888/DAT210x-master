import pandas, matched_peer
df_disagg = pandas.read_csv('C:/Users/sand9888/PycharmProjects/DAT210x-master/applied_ml/Upwork/disagg-updated.csv')
df_disagg['Month'] = pandas.to_datetime(df_disagg['Month'], format='%m/%d/%y %H:%M').dt.strftime('%y/%m/%d')

df_final = matched_peer.get_estimates(df_disagg, quant_number=10)
matched_peer.generate_report(df_final)