import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# reading dataset
root_dir = os.path.abspath('../process.csv')
filename = 'process.csv'
df = pd.read_csv(os.path.join(root_dir, filename), names = ['Timeseries', 'x'], header = 0)

#converting to timeseries format
df.Timeseries = pd.to_datetime(df.Timeseries)
df = df.set_index('Timeseries')

# visually checking data stationarity
plt.plot(df)
plt.show()

def stationarity(timeseries):
	# Determing rolling statistics
	rolmean = df.rolling(window=12,center=False).mean()
	rolstd = df.rolling(window=12,center=False).std()
	
	# Plot rolling statistics:
	orig = plt.plot(timeseries, color='blue', label='Original')
	mean = plt.plot(rolmean, color='red', label='Rolling Mean')
	std = plt.plot(rolstd, color='black', label='Rolling Std')
	plt.legend(loc='best')
	plt.title('Rolling Mean & Standard Deviation')
	plt.show()

stationarity(df)

#calculating moving average
moving_avg = df.rolling(center=False,window=12).mean()
plt.plot(df)
plt.plot(moving_avg, color='red')
#plt.show()

# substracting MA from data to remove trend
moving_avg_diff = df - moving_avg
print(moving_avg_diff.head(12))

#
moving_avg_diff.dropna(inplace=True)
stationarity(moving_avg_diff)

# differencing
df_diff = df - df.shift()
plt.plot(df_diff)
plt.show()
df_diff.dropna(inplace=True)
stationarity(df_diff)

# decomposing
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(df)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(df, label='Original')
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

# after this if data stationary we can try to forecast it using ARMA/ARIMA models


