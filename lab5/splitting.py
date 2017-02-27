from sklearn.model_selection import train_test_split
import pandas as pd

data   = [0,1,2,3,4, 5,6,7,8,9]  # input dataframe samples
labels = [0,0,0,0,0, 1,1,1,1,1]  # the function we're training is " >4 "
data_train, data_test, label_train, label_test = train_test_split(data, labels, test_size=0.5, random_state=7)

print(data_train)
print(label_train)
print(data_test)
print(label_test)



# Process:
# Load a dataset into a dataframe
X = pd.read_csv('data.set', index_col=0)

# Do basic wrangling, but no transformations
# ...

# Immediately copy out the classification / label / class / answer column
y = X['classification'].copy()
print(y)
X.drop(labels=['classification'], inplace=True, axis=1)

# Feature scaling as necessary
# ...

# Machine Learning
# ...

# Evaluation
