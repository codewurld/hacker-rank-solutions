#importing libraries
#loads dataset
import pandas as pd
#array and matrices operations
import numpy as np
#splits data to train & test
from sklearn.model_selection import train_test_split
# library for logistic regression
from sklearn.linear_model import LogisticRegression
#accurate score measure
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
#visualise dataset
import seaborn as sms
import matplotlib as plt
#avoid unnecessary information
import warnings
#to display plot continuously
%matplotlib inline
#parameters for warning
warnings.filterwarnings("ignore")

# Dataset load, preprocessing and analysis

data = pd.read_csv('Desktop/store-data/heart.csv')

#top of dataset
data.head()

#bottom of dataset
data.tail()

#amount of rows and columns in data
data.shape

#analyse data
data.info()

#missing values - returned data is clean
data.isnull().sum()

# get statistical top level insight about data 
data.describe()
