import streamlit as st
import pandas as pd
import numpy as np

def load_data():
    # Cache the data loading function
    @st.cache_data(persist=True)
    def get_data():
        df = pd.read_csv('Data/Cleaned_data/cleaned_data.csv')
        return df
    return get_data()


def show_data():
    st.title("View, Add & Download Data")

    # Load and display data
    data = load_data().drop('Unnamed: 0', axis=1, errors='ignore')
    st.dataframe(data)

    # Add a download button
    csv = data.to_csv(index=False)  # Convert DataFrame to CSV format
    st.download_button(
        label="Download",
        data=csv,
        file_name='data.csv',
        mime='text/csv',
    )

    if st.button('Add Data'):
        # Form to add new data
        with st.form("add_data_form"):
            order_id =st.text_input('Order ID')
            product = st.text_input("Product")
            quantity_ordered = st.number_input("Quantity Ordered", min_value=1, step=1)
            price = st.number_input("Price", min_value=0.0, format="%.2f")
            order_date = st.text_input("Order Date (e.g., 4/19/2019 8:46)")
            purchase_address = st.text_input("Purchase Address")
            product_category = st.selectbox("Product Category", data['Product_Category'].unique())
            city = st.text_input("City")
            
            # Submit button
            submitted = st.form_submit_button("Add Data")
            
            if submitted:
                # Append new data to the DataFrame
                new_row = {
                    "Order_ID": order_date,
                    "Product": product,
                    "Quantity_Ordered": quantity_ordered,
                    "Price": price,
                    "Order_Date": order_date,
                    "Purchase_Address": purchase_address,
                    "Product_Category": product_category,
                    "City": city
                }
                data = data.append(new_row, ignore_index=True)
                
                # Display updated data
                st.success("New data added successfully!")
                st.dataframe(data)

                # Option to save the updated DataFrame back to a CSV file
                updated_csv = data.to_csv(index=False)
                st.download_button(
                    label="Download Updated Data",
                    data=updated_csv,
                    file_name='updated_data.csv',
                    mime='text/csv',
                )

