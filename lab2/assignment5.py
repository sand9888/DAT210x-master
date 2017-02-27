from pandas.tools.plotting import andrews_curves

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')

df = pd.read_csv('C:/DAT210x-master/Module3/Datasets/wheat.data')
df = df.drop(labels=['id', 'area', 'perimeter'], axis=1)

print(df.head())

plt.figure()
andrews_curves(df, 'wheat_type', alpha=0.4)
plt.show()

