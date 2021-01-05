import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 
import joblib

df = pd.read_csv('Fish.csv')
df =pd.get_dummies(df)
X=df[['Length1', 'Length2', 'Length3', 'Height', 'Width',
       'Species_Bream', 'Species_Parkki', 'Species_Perch', 'Species_Pike',
       'Species_Roach', 'Species_Smelt', 'Species_Whitefish']]


y = df['Weight']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X_train,y_train)
y_pred = LR.predict(X_test)
print(f'the score is {LR.score(X_train, y_train)}')

from sklearn.metrics import mean_squared_error
rms = np.sqrt(mean_squared_error(y_test,y_pred))
print('rms Error :',rms)

filename = 'finalmodel.sav'
joblib.dump(LR, filename)
