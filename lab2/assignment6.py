import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
df = pd.read_csv('C:/DAT210x-master/Module3/Datasets/wheat.data')


#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
df = df.drop(labels=['id'], axis=1)
print(df.head())


#
# TODO: Compute the correlation matrix of your dataframe
print(df.corr())

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
import matplotlib.pyplot as plt

plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()


plt.show()


