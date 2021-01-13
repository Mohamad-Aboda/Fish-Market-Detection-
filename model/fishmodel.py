


import pandas as pd # reading and writing CSV etc 
import numpy as np # handling mathematical functions
import joblib

#Data Viz libraries
import matplotlib.pyplot as plt
import seaborn as sns 

#Scientific Learning libraries
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
from sklearn.model_selection import cross_val_score



df=pd.read_csv('Fish.csv')


y=df['Species']
X=df.drop(['Species'],axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


LR=LogisticRegression()

LR.fit(X_train,y_train)  #now will fit and predict

y_pred=LR.predict(X_test)

LR.score(X_test,y_test)

data={'Actual':y_test.array,'Predicted':y_pred}
res=pd.DataFrame(data)

filename = 'finalFishModel.sav'
joblib.dump(LR, filename)
