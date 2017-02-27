import sklearn.metrics as metrics
y_true = [1, 1, 2, 2, 3, 3]  # Actual, observed testing dataset values
y_pred = [1, 1, 1, 3, 2, 3]  # Predicted values from your model>>> import sklearn.metrics as metrics

print(metrics.confusion_matrix(y_true, y_pred))

import matplotlib.pyplot as plt

columns = ['Cat', 'Dog', 'Monkey']
confusion = metrics.confusion_matrix(y_true, y_pred)
plt.imshow(confusion, cmap=plt.cm.Blues, interpolation='nearest')
plt.xticks([0,1,2], columns, rotation='vertical')
plt.yticks([0,1,2], columns)
plt.colorbar()
plt.show()