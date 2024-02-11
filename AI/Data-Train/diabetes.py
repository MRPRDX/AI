import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, recall_score, precision_score
df = pd.read_csv('./op_webcam.csv')
df.head()

df['EAR'].value_counts()
X = df.drop('EAR', axis=1)
y = df['EAR']

X = np.array(X)
y = np.array(y)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = svm.SVC(kernel='')
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

acc_train = accuracy_score(y_true=y_train, y_pred=y_pred_train)
acc_test = accuracy_score(y_true=y_test, y_pred=y_pred_test)
print(acc_test, acc_train)

p = precision_score(y_test, y_pred_test)
r = recall_score(y_test, y_pred_test)
print(p,r)
