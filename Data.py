import streamlit as st
import pandas as pd

st.title("View Data")

# Load data
@st.cache_data(persist= True)
def load_data():
    data = pd.read_csv(r'C:\Users\Pc\Desktop\Data analysis\Azubi Africa\
        Career Accelerator\Capstone\Power-BI-Dashboard-Project\Data\Sales_April_2019.csv')
    return data

st.dataframe(load_data())

# st.write('Summary Statistics')
# st.write(load_data().describe())