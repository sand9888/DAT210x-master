import pandas as pd
import numpy as np
import os

# reading dataset
root_dir = os.path.abspath('../Upwork')
filename = 'disagg.csv'
df_scource = pd.read_csv(os.path.join(root_dir, filename))
df_scource.Month = pd.to_datetime(df_scource.Month,  yearfirst=True, format='%m/%d/%y %H:%M')
df_scource.Month_sep = df_scource.Month.dt.date
df_scource.Year_sep = df_scource.Month.dt.year
# df_scource.Com = df_scource.Month_sep + df_scource.Year_sep
df_scource['Month_sep'] = df_scource['Month'].apply(lambda x: str(x)[:7])
print(df_scource['Month_sep'])