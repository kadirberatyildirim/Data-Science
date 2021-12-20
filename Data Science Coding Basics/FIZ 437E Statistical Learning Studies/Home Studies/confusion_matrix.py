
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

actual = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
predicted = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
results = confusion_matrix(actual, predicted)
print('Confusion matrix : ')
print(results)
print('Accuracy score : ', accuracy_score(actual, predicted))
print('Report : ')
print (classification_report(actual, predicted))