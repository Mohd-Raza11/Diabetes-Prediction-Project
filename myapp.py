import numpy as np
import pandas as pd
import streamlit as st
import pickle

# load the model
model=pickle.load(open("Diabetes-prediction-ML-model.pkl","rb"))
# load the scaler
scaler=pickle.load(open('scaler.pkl','rb'))

def predictor(pragnancies,glucose,diastolic,triceps,insulin,bmi,dpf,age):
    x=scaler.transform(np.array([pragnancies,glucose,diastolic,triceps,insulin,bmi,dpf,age]).reshape(1,-1))
    prediction=model.predict(x)
    return prediction

def main():
    st.header(":blue[Diabetes Prediction Model]")
    st.write('''Diabetes Prediction Model is the **Classification 
         model** of **supervised learning** 
         to predict wheather a person having **Diabetes or not**.
         To do this task we give some input variables such as 
         'Pregnancies', 'Glucose', 'Diastolic', 'Triceps', 'Insulin',
          'bmi','dpf', 'age' and we will get the predicted output. ''')

    pragnancies=st.number_input('**Pregnancies**',value=None,placeholder="Type a number between  0-10") 
    glucose=st.number_input('**Glucose**',value=None,placeholder="Type a number between  0-199")
    diastolic=st.number_input('**Diastolic**',value=None,placeholder="Type a number between  0-122")
    triceps=st.number_input('**Triceps**',value=None,placeholder="Type a number between  0-99")
    insulin=st.number_input('**Insulin**',value=None,placeholder="Type a number between  0-800")
    bmi=st.number_input('**Bmi**',value=None,placeholder="Type a number between  0-100")
    dpf=st.number_input('**DPF**',value=None,placeholder="Type a number between  0-3")
    age=st.number_input('**Age**',value=None,placeholder="Type a number between  21-81")
    button=st.button(":blue[**Predict**]")
    result=""
    
    
    try:
        if button:
            result=predictor(pragnancies,glucose,
                             diastolic,triceps,
                             insulin,bmi,
                             dpf,age)
            st.success("The output is {}".format(result))
    except:
        # e = RuntimeError('This is an exception of type RuntimeError')
        st.error('Please enter all the input values')
    
    

if __name__=="__main__":
    main()


