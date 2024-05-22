import numpy as np
import pandas as pd
import streamlit as st

# load the model
# model=pickle.load(open("Diabetes_prediction.ipynb","rb"))


st.header("Diabetes Prediction Model")
st.write('''Diabetes Prediction Model is the Classification 
         model of supervised machine learning 
         to predict wheather a person having Diabetes or not.
         To do this task we give some input variables such as 
         'Pregnancies', 'Glucose', 'Diastolic', 'Triceps', 'Insulin',
          'bmi','dpf', 'age' and we will get the desired output. ''')

st.number_input('Pregnancies',value=None,placeholder="Type a number between  0-10") 
st.number_input('Glucose',value=None,placeholder="Type a number between  0-199")
st.number_input('Diastolic',value=None,placeholder="Type a number between  0-122")
st.number_input('Triceps',value=None,placeholder="Type a number between  0-99")
st.number_input('Insulin',value=None,placeholder="Type a number between  0-800")
st.number_input('Bmi',value=None,placeholder="Type a number between  0-100")
st.number_input('DPF',value=None,placeholder="Type a number between  0-3")
st.number_input('Age',value=None,placeholder="Type a number between  21-81")
st.button("Predict") 


