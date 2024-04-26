import streamlit as st
import pandas as pd 
import numpy as np 

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Dataframe')
)

if option == 'Home' or option == '':
    st.write("""# Halaman Utama""") 
elif option == 'Dataframe':
    st.write("""## Dataframe""") 
    
    df = pd.read_csv("E:\Big Data\detected_objects.csv")
    df 

    st.write("""## Draw Charts""")  

    No_Signal = df[(df['label']=='No-Signal')].count()['label']
    Hand_Signal = df[(df['label']=='Hand-Signal')].count()['label']
    label = df['label'].count()
    chart_data = pd.DataFrame(
        df, columns=['label']
    )
    total = No_Signal + Hand_Signal
    persentase = Hand_Signal / label * 100
    data = {
        'Hand-Signal': [Hand_Signal],
        'No-Signal' : [No_Signal],
        'Total Terdeteksi': [total],
        'Persentase Hand-Signal': [persentase]
    }
    table = pd.DataFrame(data, index=['Jumlah Data'])
    
    chart_data2 = order=chart_data['label'].value_counts().index[:3]
    st.bar_chart(table)

    table