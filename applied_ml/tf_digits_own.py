import os
import numpy as np
import pandas as pd
from scipy.misc import imread
import pylab
from sklearn.metrics import accuracy_score
import tensorflow as tf

# To stop potential randomness
seed = 128
rng = np.random.RandomState(seed)

root_dir = os.path.abspath('../applied_ml')
data_dir = os.path.join(root_dir, 'Train/')
print(data_dir)
sub_dir = os.path.join(root_dir, 'Train/')

# check for existence
#print(os.path.exists(root_dir))
#print(os.path.exists(data_dir))
#print(os.path.exists(sub_dir))


train = pd.read_csv(os.path.join(data_dir, 'train.csv'))
test = pd.read_csv(os.path.join(data_dir, 'test.csv'))

sample_submission = pd.read_csv(os.path.join(data_dir, 'Sample_Submission.csv'))

#print(train.head())

img_name = rng.choice(train.filename)
filepath = os.path.join(data_dir, 'Images', 'train', img_name)

img = imread(filepath, flatten=True)

pylab.imshow(img, cmap='gray')
pylab.axis('off')
#pylab.show()

#print(img)

temp = []
for img_name in train.filename:
	image_path = os.path.join(data_dir, 'Images', 'train', img_name)
	img = imread(image_path, flatten=True)
	img = img.astype('float32')
	temp.append(img)
print(temp)
train_x = np.stack(temp)
print(train_x)

temp = []
for img_name in test.filename:
	image_path = os.path.join(data_dir, 'Images', 'test', img_name)
	img = imread(image_path, flatten=True)
	img = img.astype('float32')
	temp.append(img)

test_x = np.stack(temp)

