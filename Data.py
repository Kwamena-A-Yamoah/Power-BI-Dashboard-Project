import streamlit as st
import pandas as pd

def load_data():
    # Cache the data loading function
    @st.cache_data(persist=True)
    def get_data():
        df = pd.read_csv(r'C:\Users\Pc\Desktop\Data analysis\Azubi Africa\Career Accelerator\Capstone\Power-BI-Dashboard-Project\Data\Cleaned data\cleaned_data.csv')
        df = df.drop('Unnamed: 0', axis= 1, errors= ' ignore')
        return df
    return get_data()


def show_data():
    st.title("View Data")

    # Load and display data
    data = load_data()
    st.dataframe(data)
    
    # Add a download button
    csv = data.to_csv(index=False)  # Convert DataFrame to CSV format
    st.download_button(
        label="Download",
        data=csv,
        file_name='data.csv',
        mime='text/csv',
    )
