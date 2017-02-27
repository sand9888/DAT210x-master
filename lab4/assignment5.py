import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os
from sklearn import manifold
import random, math
# Look pretty...
matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
samples = []
colors2 = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
path = 'C:/DAT210x-master/Module4/Datasets/ALOI/32'
for file in os.listdir(path):
    img = misc.imread(path+'/'+file).reshape(-1)
    samples.append(img)
    colors2.append('b')



#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
path2 = 'C:/DAT210x-master/Module4/Datasets/ALOI/32i'
for file in os.listdir(path2):
    img = misc.imread(path2+'/'+file).reshape(-1)
    samples.append(img)
    colors2.append('r')

print(colors2)
#
# TODO: Convert the list to a dataframe
samples = pd.DataFrame(samples)




#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
isomap = manifold.Isomap(n_neighbors=6, n_components=3)
isomap.fit(samples)
T = isomap.transform(samples)





#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components


def Plot2D(T, title, x, y, num_to_plot=40):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
  y_size = (max(T[:,y]) - min(T[:,y])) * 0.08


  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], marker='.',alpha=0.7,color=colors2)

Plot2D(T, '2d', 0, 1)





#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()

