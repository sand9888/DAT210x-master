import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

root_dir = os.path.abspath('../enuk')
filename = 'ENUK by ad group by month.xlsx'
df = pd.read_excel(os.path.join(root_dir, filename))
df.ix[df.Bookings == 0, 'Bookings_final'] = 0
df.ix[df.Bookings > 0, 'Bookings_final'] = 1
# df.to_csv('enuk_csv', sep=',')
print(df.head(10))