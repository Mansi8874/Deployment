import streamlit as st
import pandas as pd

st.title("Doint Streamlit")
st.write("hello")

df=pd.DataFrame({
    'Name':['Mansi','Ram','Om','Sangeeta'],
    'Marks' :[65,92,86,45]
})
st.write(df)
st.line_chart(df['Marks'])
