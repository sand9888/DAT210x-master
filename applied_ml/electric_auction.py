import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6


#dateparse = lambda dates: pd.datetime.strptime(dates, '%dd.%mm.%YYYY')
data = pd.read_csv('mrl_upwork_model_draft.csv')
data.dropna(axis=0, inplace=True)
data.reset_index(inplace=True)
data = data.drop(labels = ['index'], axis=1)
data['Date'] = pd.to_datetime(data['Date'], yearfirst=True, format = '%d.%m.%Y')
print(data['Date'].dtypes)

data = data.set_index('Date')
print(data)
#print(data['2014-02-09'])
ts = data['offered_volume']
#plt.plot(ts)
#plt.show()

from statsmodels.tsa.stattools import adfuller


def test_stationarity(timeseries):
	# Determing rolling statistics
	rolmean = timeseries.rolling(window=30,center=False).mean()
	rolstd = timeseries.rolling(center=False,window=30).std()
	
	# Plot rolling statistics:
	orig = plt.plot(timeseries, color='blue', label='Original')
	mean = plt.plot(rolmean, color='red', label='Rolling Mean')
	std = plt.plot(rolstd, color='black', label='Rolling Std')
	plt.legend(loc='best')
	plt.title('Rolling Mean & Standard Deviation')
	plt.show()
	
	# Perform Dickey-Fuller test:
	print('Results of Dickey-Fuller Test:')
	dftest = adfuller(timeseries, autolag='AIC')
	dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
	for key, value in dftest[4].items():
		dfoutput['Critical Value (%s)' % key] = value
	print(dfoutput)
test_stationarity(ts)



ts_log = np.log(ts)
moving_avg = ts_log.rolling(center=False,window=30).mean()
plt.plot(ts_log)
plt.title('Moving Average')
plt.plot(moving_avg, color='red')
plt.show()

ts_log_moving_avg_diff = ts_log - moving_avg
#print(ts_log_moving_avg_diff.head(30))
ts_log_moving_avg_diff.dropna(inplace=True)
test_stationarity(ts_log_moving_avg_diff)

expwighted_avg = ts_log.ewm(ignore_na=False,min_periods=0,adjust=True,halflife=30).mean()
plt.plot(ts_log)
plt.title('Weighted moving average')
plt.plot(expwighted_avg, color='red')
plt.show()
ts_log_ewma_diff = ts_log - expwighted_avg
test_stationarity(ts_log_ewma_diff)

#Differencing
ts_log_diff = ts_log - ts_log.shift()
plt.title('Differencing')
plt.plot(ts_log_diff)
plt.show()
ts_log_diff.dropna(inplace=True)
test_stationarity(ts_log_diff)

#Decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(ts_log)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(ts_log, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal,label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
plt.show(block=False)

