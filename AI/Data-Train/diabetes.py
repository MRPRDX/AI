import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.tree import DecisionTreeClassifier as DTC
df = pd.read_csv("Drowsy.csv")
df.head()

df['Label'].value_counts()
X = df.drop('Label', axis=1)
y = df['Label']

X = np.array(X)
y = np.array(y)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model1 = svm.SVC(kernel="rbf")
# model1.fit(X_train, y_train)

model2 = knn(n_neighbors=2)
model2.fit(X_train, y_train)

# model2 = DTC(random_state=0)
# model2.fit(X_train, y_train)

# y_pred_train1 = model1.predict(X_train)
# y_pred_test1 = model1.predict(X_test)

y_pred_train2 = model2.predict(X_train)
y_pred_test2 = model2.predict(X_test)


# acc_train1 = accuracy_score(y_true=y_train, y_pred=y_pred_train1)
# acc_test1 = accuracy_score(y_true=y_test, y_pred=y_pred_test1)
# print(acc_test1, acc_train1)
#
# p1 = precision_score(y_test, y_pred_test1)
# r1 = recall_score(y_test, y_pred_test1)
# print(p1,r1)

acc_train2 = accuracy_score(y_true=y_train, y_pred=y_pred_train2)
acc_test2 = accuracy_score(y_true=y_test, y_pred=y_pred_test2)
print(acc_test2, acc_train2)

p2 = precision_score(y_test, y_pred_test2)
r2 = recall_score(y_test, y_pred_test2)
print(p2,r2)





