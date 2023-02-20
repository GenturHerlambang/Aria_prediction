import streamlit as st
import lab1
import lab2

navigation = st.sidebar.selectbox('Pilih Halaman : ', ('lab1', 'lab2'))

if navigation == 'lab1' :
    lab1.run()
else:
    lab2.run()