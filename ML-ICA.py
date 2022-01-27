#importing libraries
#loads dataset
import pandas as pd
#array and matrices operations
import numpy as np
#splits data to train & test
from sklearn.model_selection import train_test_split
# library for logistic regression
from sklearn.linear_model import LogisticRegression
fromsklearn.metrics import classification_report, confusion_matrix
#accurate score measure
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
#label encoder
from sklearn.preprocessing import LabelEncoder
#visualise dataset
import seaborn as sms
import matplotlib as plt
#avoid unnecessary information
import warnings
#to display plot continuously
%matplotlib inline
#parameters for warning
warnings.filterwarnings("ignore")

# Data Analysis
data = pd.read_csv('Desktop/store-data/heart.csv')

#top of dataset
data.head()

#bottom of dataset
data.tail()

# Data Encoding
#encoding data with label encoder to convert columns with text values

le = LabelEncoder()

data['ChestPainType'] = le.fit_transform(data['ChestPainType'])
data['RestingECG'] = le.fit_transform(data['RestingECG'])
data['ExerciseAngina'] = le.fit_transform(data['ExerciseAngina'])
data['ST_Slope'] = le.fit_transform(data['ST_Slope'])

data.tail()

#amount of rows and columns in data
data.shape

#analyse data
data.info()

#check for missing values - returned data is clean
data.isnull().sum()

# get statistical top level insight about data 
data.describe()

#distribution of sex
data['Sex'].value_counts()

#distribution of exercise induced angina
data['ExerciseAngina'].value_counts()

## Data Cleaning
#remove sex column
updated_data = data.drop(columns="Sex", axis=1)

#input and output values
x = updated_data
y = updated_data['HeartDisease'] # 0 = False, 1 = True

# separating training and test data - 70:30

x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.3,random_state=0)

print(x.shape, x_train.shape, x_test.shape)

### Model Training
model = LogisticRegression(solver='liblinear',
                           C=0.05,multi_class='ovr',
                           random_state=0)

model.fit(x_train, y_train)

### Model Evaluation

#determine model accuracy and likelihood of overfitting
y_pred = model.predict(x_test)

model.score(x_train,y_train)
model.score(x_test,y_test)

#### Confusion Matrix
cm = confusion_matrix(y_test, y_pred)


