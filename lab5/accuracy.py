from sklearn.metrics import accuracy_score

# Returns an array of predictions:
predictions = my_model.predict(data_test)
predictions
[0, 0, 0, 1, 0]

# The actual answers:
label_test
[1, 1, 0, 0, 0]

accuracy_score(label_test, predictions)
0.4000000000000000

accuracy_score(label_test, predictions, normalize=False)
2