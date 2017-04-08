import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib.ticker as plticker

root_dir = os.path.abspath('../Upwork')
filename_cons = '01e19194-2792-46cb-b94f-17f041210c97_consumption.csv'
filename_temp = '01e19194-2792-46cb-b94f-17f041210c97_temperature.csv'
df_cons = pd.read_csv(os.path.join(root_dir, filename_cons))
df_temp = pd.read_csv(os.path.join(root_dir, filename_temp ))
df_cons['Date'] = pd.to_datetime(df_cons['Date'], yearfirst=True, format='%Y-%m-%d')
df_temp['Date'] = pd.to_datetime(df_temp['Date'], yearfirst=True, format='%Y-%m-%d')

id_cons = (str(os.path.splitext(os.path.split(filename_cons)[1])[0])).split('_')[0]
id_temp = (str(os.path.splitext(os.path.split(filename_temp)[1])[0])).split('_')[0]

col = 'Value'
fig = plt.figure(figsize=(22, 6))  
for i in range(15,4,-1):
	temp1 = df_cons.ix[(df_cons.Date == ('2017-03-'+str(i))) & (df_cons.Hour >= 0) & (df_cons.Hour <= 23)]
	print(temp1.shape)
	temp0 = df_temp.ix[(df_temp.Date == ('2017-03-'+str(i))) & (df_temp.Hour >= 0) & (df_temp.Hour <= 23)]
	
	
	
	ax1 = fig.add_subplot(1, 2, 1)
	ax0 = fig.add_subplot(1, 2, 2)
	ax0.set_title('Plot of ' + col + '\n for temperature ' + '\n id=' + id_temp)
	ax0.set_ylabel('Temperature')
	ax0.set_xlabel('Hours') 
	ax1.set_ylabel('Consumption')  
	ax1.set_xlabel('Hours')
	
	ax1.set_title('Plot of ' + col + '\n for consumption ' + '\n id=' + id_cons)
	loc = plticker.MultipleLocator(base=2.0)
	ax1.xaxis.set_major_locator(loc)
	ax0.xaxis.set_major_locator(loc)
	
	
	ax0.plot(temp0.Hour, temp0.Value)
	ax1.plot(temp1.Hour, temp1.Value)
	
plt.show()
	
'''col = 'Value'
temp1 = df_cons.ix[(df_cons.Date == '2017-03-15') & (df_cons.Hour >= 0) & (df_cons.Hour <= 23), col]
temp0 = df_temp.ix[(df_temp.Date == '2017-03-15') & (df_temp.Hour >= 0) & (df_temp.Hour <= 23), col]
fig = plt.figure(figsize=(12, 6))
fig.clf()
ax1 = fig.add_subplot(1, 2, 1)
ax0 = fig.add_subplot(1, 2, 2)
ax1.plot(temp1.as_matrix())
ax1.set_title('Plot of ' + col + '\n for consumption on 2017-03-15 ' + '\n id=' + id_cons)
ax0.plot(temp0.as_matrix())
ax0.set_title('Plot of ' + col + '\n for temperature on 2017-03-15 ' + '\n id=' + id_temp)
plt.show()   '''

