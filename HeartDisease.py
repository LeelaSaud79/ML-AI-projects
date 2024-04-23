# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:43:39 2024

@author: user
"""

#import numpy as np
import pandas as pd
import pickle

loaded_model = pickle.load(open('C:/Users/user/Desktop/Final Project/HeartDisease_Prediction_System/heart.sav' , 'rb'))

X_test = pd.DataFrame({'age':[52], 'sex':[1], 'cp':[0], 'trestbps':[125], 'chol':[212], 'fbs':[0], 'restecg':[1], 'thalach':[168], 'exang':[0], 'oldpeak':[1], 'slope':[2], 'ca':[2], 'thal':[3]})
input_data = (X_test)

# Change the input data to a numpy array
#input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for only one instance
#input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(X_test)

print(prediction)

if prediction[0] == 0:
  print('The person is not heart patient')
else:
  print('The person is heart patient')