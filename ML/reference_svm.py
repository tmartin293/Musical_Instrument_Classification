"""
Example output: 
  accuracy = 0.9814705882352941
  precision = 0.9828141786871974
  recall = 0.9814705882352941
  fi = 0.9821418595420995
"""

from sklearn import svm
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score, precision_score, recall_score
from csv import reader

def load_csv(filename):
    file = open(filename, "rt")
    lines = reader(file)
    dataset = list(lines)
    dataset = np.array(dataset).astype('float')
    predictors = dataset[:,0:13]
    labels = dataset[:,13].astype('int')
    return predictors, labels
    
def SVM(train_data, train_labels, test_data, test_labels):
    svm_clsf = svm.SVC(C=50.0, kernel='rbf', gamma=0.005, decision_function_shape='ovr')
    svm_clsf.fit(train_data, train_labels)
    test_predictions = svm_clsf.predict(test_data)
    accuracy = accuracy_score(test_labels, test_predictions)
    precision = precision_score(test_labels, test_predictions, average='weighted')
    recall = recall_score(test_labels, test_predictions, average='weighted')
    f1 = 2.0 * (precision * recall) / (precision + recall)
    print( (accuracy),(","),(precision),(", "),(recall),(", "),(fi) )
    return accuracy, precision, recall, f1

sss = StratifiedShuffleSplit(n_splits=5, test_size=0.125)
metrics = []
filename = 'mfcc_results.csv'
X_data, Y_data = load_csv(filename)
i = 0
for train_indices, test_indices in sss.split(X_data, Y_data):
    train_data, test_data = X_data[train_indices], X_data[test_indices]
    train_labels, test_labels = Y_data[train_indices], Y_data[test_indices]
    metrics.append(SVM(train_data, train_labels, test_data, test_labels))
n_splits = 0.00
accuracy = 0.00
precision = 0.00
recall = 0.00
fi = 0.00
for i in metrics:
        accuracy += i[0]
        precision += i[1]
        recall += i[2]
        fi += i[3]
        n_splits += 1
accuracy = accuracy/n_splits
precision = precision/n_splits
recall = recall/n_splits
fi = fi/n_splits
print( (accuracy),(","),(precision),(", "),(recall),(", "),(fi) )        