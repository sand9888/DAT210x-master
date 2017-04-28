import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import pandas as pd

root_dir = os.path.abspath('../Upwork')
filename = 'test.csv'
df = pd.read_csv(os.path.join(root_dir, filename))
df['Start Time'] = pd.to_datetime(df['Start Time'], unit='s')
df.Date.apply(str)



def best_rectangle(date, amplitude_threshold=0):
	dataframe = df[df.Date == date]
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)
	plt.xlim([0, 24])
	plt.ylim([0, dataframe['Amplitude'].max() + 300])
	for i, (starttime, duration, amplitude, hour, nth_hour, value) in enumerate(zip(dataframe['Start Time'], dataframe['Duration'], dataframe['Amplitude'],
													dataframe['Hour'], dataframe['nth Hour'], dataframe['Value'])):
		
		ax1.add_patch(
    		patches.Rectangle(
        		((hour-nth_hour), 0),   # (x,y)
				duration,          # width
        		amplitude, fill=False,  linewidth=0.5, alpha=0.5   # height
    		)
		)
	
		if df.ix[i, 'Amplitude'] == df.ix[i+1, 'Amplitude']:
			value_list.append(df.ix[i, 'Value'])
		elif i > 0 and df.ix[i, 'Amplitude'] != df.ix[i + 1, 'Amplitude'] and df.ix[i, 'Amplitude'] == df.ix[
					i - 1, 'Amplitude']:
			value_list.append(df.ix[i, 'Value'])
			plt.text(hour - nth_hour, amplitude + 100, max(value_list), fontdict=None, withdash=False)
			print(value_list)
			value_list = []
		elif i > 0 and df.ix[i, 'Amplitude'] != df.ix[i + 1, 'Amplitude'] and df.ix[i, 'Amplitude'] != df.ix[
					i - 1, 'Amplitude']:
			value_list.append(df.ix[i, 'Value'])
			plt.text(hour - nth_hour, amplitude + 100, max(value_list), fontdict=None, withdash=False)
	plt.show()

best_rectangle('2015-01-01')