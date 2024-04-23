# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:43:40 2024

@author: user
"""

#import numpy as np
import pandas as pd
import pickle
import streamlit as st

#loading saved model
loaded_model = pickle.load(open('C:/Users/user/Desktop/Final Project/HeartDisease_Prediction_System/heart.sav' , 'rb'))


#creating a function for prediction

def heart_prediction(input_data):

    X_test = pd.DataFrame({'age':[52], 'sex':[1], 'cp':[0], 'trestbps':[125], 'chol':[212], 'fbs':[0], 'restecg':[1], 'thalach':[168], 'exang':[0], 'oldpeak':[1], 'slope':[2], 'ca':[2], 'thal':[3]})
    #input_data = (X_test)

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

def main():
    
    #giving a title
    
    st.title('Heart Disease Prediction Web App')
    
    #getting the input data from the user
    
    age= st.text_input('Enter your age')
    sex = st.text_input('SEX')
    cp = st.text_input('cp value')
    trestbps = st.text_input('trestbps value')
    chol = st.text_input('chol value')
    fbs = st.text_input('fbs value')
    restecg = st.text_input('restecg value')
    thalach = st.text_input('thalach value')
    exang = st.text_input('exang value')
    oldpeak = st.text_input('oldpeak value')
    slope = st.text_input('slope value')
    ca = st.text_input('ca value')
    thal = st.text_input('thal value')
    
    #code for Prediction
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Heart Disease Test Result'):
        
        diagnosis = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()