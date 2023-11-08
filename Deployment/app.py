import streamlit as st
import eda
import prediction

navigaation = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Predict a Turnover'))

if navigaation == 'EDA':
    eda.run()
else:
    prediction.run()
