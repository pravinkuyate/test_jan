import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score


data=pd.read_csv(r"C:\Users\pravinkuyate\OneDrive\Desktop\DS and ALGO\Wholesale customers data.csv")
data.head()
data.info()
X = data.drop(columns=['Channel'])  
y = data['Channel']


y = y.map({1: 0, 2: 1})


model = XGBClassifier()


accuracy_scores = cross_val_score(model, X, y, cv=5)


mean_accuracy = np.mean(accuracy_scores)
print("Mean Accuracy:", mean_accuracy)