import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config (
    page_title= 'Turnover Prediction - EDA',
    layout = 'wide',
    initial_sidebar_state='expanded'
    )

def run():
        #membuat title
        st.title('Turnover Prediction')

        #membuat sub_header
        st.subheader('EDA untuk Analisis Payment Credit Card')


        #menambahkan gambar
        st.image('foto.jpg')

        # Menambahkan deskripsi
        st.write('Project Createn by Stephanus Adinata (SBY-001)')


        #membuat garis lurus
        st.markdown('---')

        #Magic Syntax
        '''
        On this Page we will do a simple exploration,
        Used Database is Credit Card Default Payment.
        Dataset Source is from Kaggle
        '''

        #show dataframe
        st.title('Dataset')
        df = pd.read_csv('Employee.csv')
        st.dataframe(df)

        #membuat barplot 
        st.write('### Plot Leave or Not')
        fig = plt.figure(figsize=(15,5))
        sns.countplot(x='LeaveOrNot', data=df)
        st.pyplot(fig)
        st.write('Karyawan mayoritas tidak Resign')
        st.markdown('---')

        #membuat barplot 
        st.write('### Plot Joining Year')
        fig = plt.figure(figsize=(15,5))
        sns.countplot(x='JoiningYear' , hue = 'LeaveOrNot', data = df)
        st.pyplot(fig)
        st.write('Tahun 2018 adalah tahun dimana karyawan paling banyak resign')
        st.markdown('---')


        #membuat barplot 
        st.write('### Plot Gender')
        fig = plt.figure(figsize=(15,5))
        sns.countplot(x='Gender', hue = 'LeaveOrNot', data=df)
        st.pyplot(fig)
        st.write('Mayoritas Karyawan pada dataset yang resign adalah perempuan / female')
        st.markdown('---')

        #membuat barplot 
        st.write('### Plot Payment Tier')
        fig = plt.figure(figsize=(15,5))
        sns.countplot(x='PaymentTier', hue = 'LeaveOrNot', data=df)
        st.pyplot(fig)
        st.write('Dari grafik di atas diketahui bahwa mayoritas karyawan yang resign adalah karyawan yang menerima payment di tier 2')
        st.markdown('---')

if __name__ == '__main___':
    run()