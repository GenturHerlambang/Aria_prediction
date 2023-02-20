import streamlit as st
import pandas as pd
import numpy as np
import pickle


with open('model1.pkl', 'rb') as file_1:
  model1 = pickle.load(file_1)

  
with open('scaler.pkl', 'rb') as file_3:
  skaler = pickle.load(file_3)









def run() :
 st.title('Prediksi untuk Lab 1')
 with st.form(key='form_parameters'):
     v1 = st.number_input('v1', min_value=0, max_value=1000, value=500)
     v2 = st.number_input('v2', min_value=0, max_value=1000, value=500)
     v3 = st.number_input('v3', min_value=0, max_value=1000, value=500)
     v4 = st.number_input('v4', min_value=0, max_value=1000, value=500)
     v5 = st.number_input('v5', min_value=0, max_value=1000, value=500)
     v6 = st.number_input('v6', min_value=0, max_value=1000, value=500)
     v7 = st.number_input('v7', min_value=0, max_value=1000, value=500)
     v8 = st.number_input('v8', min_value=0, max_value=1000, value=500)
    

     submitted = st.form_submit_button('Predict')


 data_inf = {
    'v1': v1, 
    'v2': v2, 
    'v3': v3, 
    'v4': v4, 
    'v5': v5, 
    'v6': v6,
    'v7': v7, 
    'v8': v8, 
    
 }
 data_inf = pd.DataFrame([data_inf])
 st.dataframe(data_inf)

 if submitted:

    # Feature Scaling and Feature Encoding
    data_inf_num_scaled = skaler.transform(data_inf)
 
    # Predict using Linear Regression
    y_pred_inf = model1.predict(data_inf_num_scaled)
    
    st.write(' Target : ', (y_pred_inf))