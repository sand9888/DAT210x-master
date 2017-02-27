import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from  mpl_toolkits.mplot3d import Axes3D
'''df = pd.read_csv('C:/DAT210x-master/Module2/Datasets/direct_marketing.csv')
print(df.head())
df.recency[ df.recency < 7 ] = 'abc'
print(df.head(10))

ordered_satisfaction = ['Mad', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
df = pd.DataFrame({'satisfaction':['Mad', 'Happy', 'Unhappy', 'Neutral']})
df.satisfaction = df.satisfaction.astype("category",
  ordered=True,
  categories=ordered_satisfaction
).cat.codes
print(df)

from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Authman ran faster than Harry because he is an athlete.","Authman and Harry ran faster and faster."]
bow = CountVectorizer()
X = bow.fit_transform(corpus)
print(bow.get_feature_names())
print(X.toarray())

df = pd.read_csv('C:/DAT210x-master/students.data', index_col=0)
print(df.head())
my_series = df.G3
my_dataframe = df[['G1', 'G2', 'G3']]
plt.style.use('ggplot')
#my_series.plot.hist(alpha = 0.5, normed=True)
#my_dataframe.plot.hist(alpha = 0.5, normed=True)
df.plot.scatter(x='G1', y='G3')
plt.show()

df = pd.read_csv('C:/DAT210x-master/students.data', index_col=0)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')

ax.scatter(df.G1, df.G3, df['Dalc'], c='r', marker='.')
plt.show()

from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')
# If the above line throws an error, use plt.style.use('ggplot') instead

# Load up SKLearn's Iris Dataset into a Pandas Dataframe
data = load_iris()
print(data.target)
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target_names'] = [data.target_names[i] for i in data.target]
print(df.head(20))

plt.figure()
parallel_coordinates(df, 'target_names')
plt.show()'''
df = pd.read_csv('C:/Users/sand9888/Downloads/train.csv')
df.Age = df.Age.fillna(df.Age.median())
df = df.drop(labels=['Cabin', 'Name', 'Ticket'], axis=1)
print(df.head())





