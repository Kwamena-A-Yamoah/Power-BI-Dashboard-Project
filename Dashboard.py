import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    # Cache the data loading function
    @st.cache_data(persist=True)
    def get_data():
        df = pd.read_csv(r'C:\Users\Pc\Desktop\Data analysis\Azubi Africa\Career Accelerator\Capstone\Power-BI-Dashboard-Project\Data\Cleaned data\cleaned_data.csv')
        df = df.drop('Unnamed: 0', axis= 1, errors= ' ignore')
        return df
    return get_data()

# columns = ['Product', 'Quantity_Ordered', 'Price', 'Order_Date'
# ,'Purchase_Address']

df = load_data()
def show_dashboard():

    # # Sidebar filters
    # st.sidebar.header("Please filter")
    # category = st.sidebar.multiselect(
    #     "Select Product Category",
    #     options=df["Product_Category"].unique(),
    #     default=df["Product_Category"].unique(),
    # )
    # product = st.sidebar.multiselect(
    #     "Select Product",
    #     options=df["Product"].unique(),
    #     default=df["Product"].unique(),
    # )
    # city = st.sidebar.multiselect(
    #     "Select City",
    #     options=df["City"].unique(),
    #     default=df["City"].unique(),
    # )
        # Apply filters
    # filtered_df = df[
    #     (df["Product_Category"].isin(category)) &
    #     (df["Product"].isin(product)) &
    #     (df["City"].isin(city))
    # ]
# columns = ['Product', 'Quantity_Ordered', 'Price', 'Order_Date', 'Purchase_Address']
    
# =================================================================================================

    # compute top analytics
    total_sales = (df["Price"] * df["Quantity_Ordered"]).sum()
    total_orders = (df["Quantity_Ordered"]).sum()
    average_sales = total_sales/total_orders
    
    col1,col2,col3 = st.columns(3)
    with col1:
        st.info('Total Revenue')
        st.metric(label="Total Sales", value=f"${total_sales:,.0f}")
    
    with col2:
        st.info('Average Sales Per Order')
        st.metric(label="Average Sales", value=f"${average_sales:,.1f}")
    
    with col3:
        st.info('Total Orders')
        st.metric(label="Total Orders", value=f"{total_orders:,.0f}")
    
# =================================================================================================

    # Calculate total Sales
    df['Total_Sales'] = df["Price"] * df["Quantity_Ordered"]
    
    # Group by Product and total sales
    product_sales = df.groupby('Product').agg({'Quantity_Ordered': 'sum', 'Total_Sales': 'sum'})
    
    # Sortings
    sorted_sales = product_sales.sort_values(by='Total_Sales', ascending=False)
    sorted_orders = product_sales.sort_values(by='Quantity_Ordered', ascending=False)
    
    col1,col2 = st.columns(2)
    with col1:
        # Visualization Product and total sales
        st.plotly_chart(px.bar(sorted_sales, y="Total_Sales", title="Products by Sales", orientation='h'))
    
    with col2:
        # Visualization Product and total orders
        st.plotly_chart(px.bar(sorted_orders, y="Quantity_Ordered", title=" Products by Orders", orientation='h'))
    
# =================================================================================================

    # Convert Order_date to date format
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    
    # Creating a month column
    df['Month'] = df['Order_Date'].dt.month
    
    # setting a dictionary to map out the month names
    monthname = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    # Group by month and sum total sales
    monthly_sales = df.groupby('Month')['Total_Sales'].sum()

    # Map the month numbers to month names
    monthly_sales.index = monthly_sales.index.map(monthname)
    
    # Visualize Month with total sales using plotly
    st.plotly_chart(px.line(monthly_sales, title="Monthly Sales"))

# =================================================================================================

    monthly_orders = df.groupby('Month')['Quantity_Ordered'].sum()

    # Map the month numbers to month names
    monthly_orders.index = monthly_orders.index.map(monthname)
    
    # Visualize Month with total sales using plotly
    st.plotly_chart(px.line(monthly_orders, title="Monthly Orders"))

# =================================================================================================

    


    
            