import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

ts=robjects.r('ts')
forecast = importr("forecast", lib_loc = "C:/Users/sand9888/Documents/sand9888/R/win-library/3.3")
import os
import pandas as pd

from rpy2.robjects import pandas2ri
pandas2ri.activate()


train = os.path.join('C:/DAT203.3x/Lab01/cadairydata.csv')
traindf=pd.read_csv(train, index_col=0)
traindf.index=traindf.index.to_datetime()

rdata=ts(traindf.Price.values,frequency=4)
fit=forecast.auto_arima(rdata)
forecast_output=forecast.forecast(fit,h=16,level=(95.0))