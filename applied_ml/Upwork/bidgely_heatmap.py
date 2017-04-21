import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import seaborn as sns; sns.set()
import re
uniform_data = np.random.rand(10, 12)
import matplotlib.ticker as plticker

# reading dataset
root_dir = os.path.abspath('../Upwork')
filename = 'test.csv'
df = pd.read_csv(os.path.join(root_dir, filename))
df2 = df[['Date', 'Hour', 'Value']]
df2.Date.apply(str)


df2 = pd.pivot_table(df2,index=["Date"], columns='Hour', values='Value')
x = [1,3,5,6]
ax = sns.heatmap(df2, cmap="YlGnBu")
for label in ax.get_yticklabels():
	# print(label.get_text())
	if label.get_text()  in ['2015-01-01', '2015-02-01', '2015-03-01', '2015-04-01', '2015-05-01',
							 '2015-06-01', '2015-07-01', '2015-08-01', '2015-09-01', '2015-10-01',
							 '2015-11-01', '2015-12-01'] :
		
		label.set_size(10)
		label.set_color("black")
	else:
		label.set_size(0)
		label.set_weight("bold")
		label.set_color("white")

#yticks = np.linspace(1,12, 12)
#ax.set_yticks(yticks*ax.get_ylim()[1])
plt.yticks(rotation=0)
plt.show()

