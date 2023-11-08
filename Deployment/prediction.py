import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

with open('model.pkl', 'rb') as file_1:
     model = pickle.load(file_1) 



def run():
    with st.form(key='Form Parameters'):
        Name = st.text_input('Name', value='')
        Gender =  st.selectbox('Sex', ('Male', 'Female'), index=1)
        Education =  st.selectbox('Education', ('1', '2', '3'), index=1, help='1=Bachelor , 2=Master, 3=PHD')
        Age = st.number_input('Umur', min_value=22, max_value=41, step=1, help='Usia Karyawan')
        Joining_Year = st.number_input('Joining Year', min_value=2012, max_value=2018, step=1)
        PaymentTier = st.number_input('Payment Tier', min_value=1, max_value=3, step=1)
        EverBenched = st.selectbox('Ever Benched', ('Yes', 'No'), index=1)
        ExperienceInCurrentDomain = st.number_input('Experience In Current Domain', min_value=0, max_value=7, step=1)
        st.markdown('---')
        submitted = st.form_submit_button('Predict')

    data_inf = {'Education': int(Education),
    'JoiningYear': int(Joining_Year),
    'PaymentTier': int(PaymentTier),
    'Age': int(Age),
    'EverBenched': EverBenched,
    'ExperienceInCurrentDomain': int(ExperienceInCurrentDomain)}

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
            
            # predict result
            y_predict_inf = model.predict(data_inf)# predict result
            if y_predict_inf == 1: 
                st.write('# Resign')
            else:
                st.write('# Stay')

if __name__ == '__main___':
    run()
