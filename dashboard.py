import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def load_data():
    # Cache the data loading function
    @st.cache_data(persist=True)
    def get_data():
        df = pd.read_csv(r'C:\Users\Pc\Desktop\Data analysis\Azubi Africa\Career Accelerator\Capstone\Power-BI-Dashboard-Project\Data\Cleaned data\cleaned_data.csv')
        df = df.drop('Unnamed: 0', axis= 1, errors= ' ignore')
        return df
    return get_data()

# columns = ['Product', 'Quantity_Ordered', 'Price', 'Order_Date','Purchase_Address']

df = load_data()


# Add a new column for total sales and price categor
df['Total_Sales'] = df['Quantity_Ordered']*df['Price']
df['price_category'] = np.where(df['Price'] > 99.99, 'High-Level Product', 'Basic Level Product')



def show_dashboard():
    
    # Convert Order_date to date format
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    
     # Convert Order_date to date format
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    
    # Extract the year
    df['Year'] = df['Order_Date'].dt.year
    
    # Extract month names
    df['Month'] = df['Order_Date'].dt.month_name()
    
    # # Sidebar filters
    # st.sidebar.header("Please filter")
    # year = st.sidebar.multiselect(
    #     "Select Year",
    #     options=df["Year"].unique(),
    #     default=df["Year"].unique(),
    # )
    # month = st.sidebar.multiselect(
    #     "Select Month",
    #     options=df["Month"].unique(),
    #     default=df["Month"].unique(),
    # )
    # city = st.sidebar.multiselect(
    #     "Select City",
    #     options=df["City"].unique(),
    #     default=df["City"].unique(),
    # )
    # product_category = st.sidebar.multiselect(
    #     "Select Product Category",
    #     options=df["Product_Category"].unique(),
    #     default=df["Product_Category"].unique(),
    # )
    #     # Apply filters
    # filtered_df = df[
    #     (df["Year"].isin(year)) &
    #     (df["Month"].isin(month)) &
    #     (df["City"].isin(city)) &
    #     (df["Product_Category"].isin(product_category))
    # ]
    
    # Sidebar filters
    st.sidebar.header("Please filter")

    # Year filter with "All" option
    selected_year = st.sidebar.multiselect(
        "Select Year",
        options=["All"] + df["Year"].unique().tolist(),
        default=["All"]
    )

    # Month filter with "All" option
    selected_month = st.sidebar.multiselect(
        "Select Month",
        options=["All"] + df["Month"].unique().tolist(),
        default=["All"]
    )

    # City filter with "All" option
    selected_city = st.sidebar.multiselect(
        "Select City",
        options=["All"] + df["City"].unique().tolist(),
        default=["All"]
    )

    # Product Category filter with "All" option
    selected_product_category = st.sidebar.multiselect(
        "Select Product Category",
        options=["All"] + df["Product_Category"].unique().tolist(),
        default=["All"]
    )

    # Apply filters (filter only if 'All' is not selected)
    filtered_df = df[
        (df["Year"].isin(df["Year"].unique()) if "All" in selected_year else df["Year"].isin(selected_year)) &
        (df["Month"].isin(df["Month"].unique()) if "All" in selected_month else df["Month"].isin(selected_month)) &
        (df["City"].isin(df["City"].unique()) if "All" in selected_city else df["City"].isin(selected_city)) &
        (df["Product_Category"].isin(df["Product_Category"].unique()) if "All" in selected_product_category else df["Product_Category"].isin(selected_product_category))
    ]

# columns = ['Product', 'Quantity_Ordered', 'Price', 'Order_Date', 'Purchase_Address']
    
    
# =================================================================================================

    if st.button('Descriptive Summary'):

        # Display the descriptive statistics
        summary = df.describe().T  # Include all columns, including non-numeric

        # Show the summary in Streamlit
        st.write(summary)
    
# =================================================================================================
   
    # compute top analytics
    total_sales = (filtered_df["Price"] * filtered_df["Quantity_Ordered"]).sum()
    total_orders = (filtered_df["Quantity_Ordered"]).sum()
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

    st.write('___')   
 # =================================================================================================
    
    st.subheader('Bar chart')

    # Select X and Y axes from the DataFrame
    col1,col2 = st.columns(2)
    with col1:
        x_axis1 = st.selectbox('X-Axis', filtered_df.drop('Order_Date', axis=1).columns)
    
    with col2:
        y_axis1 = st.selectbox('Y-Axis', filtered_df.drop('Order_Date', axis=1).columns)
    
    # Sort the data by the Y-Axis column in descending order
    df_sorted = filtered_df.sort_values(by=y_axis1, ascending=False)

    fig = px.bar(df_sorted, x=x_axis1, y=y_axis1, title=f'{y_axis1} vs {x_axis1}')
        
    # Display the chart
    st.plotly_chart(fig)

# =================================================================================================

    # Creating a month column
    filtered_df['Month_num'] = filtered_df['Order_Date'].dt.month
        
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
    
    # Group total sales by month
    monthly_sales = filtered_df.groupby('Month_num')['Total_Sales'].sum()

    # Map the month numbers to month names
    monthly_sales.index = monthly_sales.index.map(monthname)
        
    # Visualize Month with total sales using plotly
    fig= px.line(monthly_sales, title="Monthly Sales")
    fig.update_layout(
    showlegend=False,
    yaxis_title="Sales",
    xaxis_title="",
    )

    # st.plotly_chart(fig)

    # ====================================

    # Group total orders by month
    monthly_orders = filtered_df.groupby('Month_num')['Quantity_Ordered'].sum()

    # Map the month numbers to month names
    monthly_orders.index = monthly_orders.index.map(monthname)
        
    # Visualize Month with total sales using plotly
    fig1= px.line(monthly_orders, title="Monthly Orders")
    fig1.update_layout(
        showlegend=False,
        yaxis_title="Orders",
        xaxis_title=""
    )
    # st.plotly_chart(fig)

# ====================================

    left,right = st.columns(2)
    left.plotly_chart(fig, use_container_width=True)
    right.plotly_chart(fig1, use_container_width=True)
   
# =================================================================================================
# =================================================================================================

    if st.button('Show More Analysis'):

        # Scatter plot of data
        st.subheader('Scatter Plot')
        
        # Get continuous features
        continuous_features = filtered_df.select_dtypes(include=['float64', 'int64']).columns

        # Set default selections for 'Quantity_Ordered' and 'Total_Sales'
        default_y = 'Price' if 'Price' in continuous_features else continuous_features[0]
        default_x = 'Total_Sales' if 'Total_Sales' in continuous_features else continuous_features[1]

        # Place in columns
        col1, col2 = st.columns(2)
        with col1:
            # Select X and Y axes from the continuous features with defaults
            x_axis = st.selectbox('X-Axis', continuous_features, index=list(continuous_features).index(default_x))
    
        with col2:
            y_axis = st.selectbox('Y-Axis', continuous_features, index=list(continuous_features).index(default_y))
            # Create the scatter plot
            
        fig = px.scatter(filtered_df, x=x_axis, y=y_axis,
                        title=f'{y_axis} to {x_axis}'
                        )

        # Display the chart
        st.plotly_chart(fig)
        
    # =================================================================================================   
            
    # Compute the correlation matrix
        corr_matrix = filtered_df.select_dtypes(include=['float64','int64']).corr()

        # Create a heatmap using plotly.express
        fig = px.imshow(corr_matrix, 
                        text_auto=True,  # Display correlation values on the heatmap
                        color_continuous_scale='Reds', 
                        aspect='auto', 
                        title="Correlation Heatmap")

        # Display the heatmap in Streamlit
        st.plotly_chart(fig)    
        
# =================================================================================================

        # Box and Violin Plots
        # Create a subheader for the plots
        st.subheader('Box Plot and Violin Plot')

        # Select feature to plot
        feature = st.selectbox('Select Feature', continuous_features)

        if feature:
            # Create the box plot for the selected feature
            fig_box = px.box(filtered_df, y=feature, title=f'Box Plot')
            
            # Create the violin plot for the selected feature
            fig_violin = px.violin(filtered_df, y=feature, title=f'Violin Plot')
            
            # Display the plots in columns
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(fig_box)
            with col2:
                st.plotly_chart(fig_violin)

    

# =================================================================================================
    
    st.write(f"""
    1. Overall Performance: The total revenue generated is ${total_sales:,.2f} from {total_orders:,.0f} orders, 
       Throughout the year.

    2. Product Insights: The scatter plot and bar charts reveal relationships between product quantities, prices, and total sales.

    3. Monthly Patterns: The line charts show clear patterns in monthly sales and order quantities, which can be used for forecasting and inventory planning.

    4. Correlations: The heatmap reveals interesting relationships between variables, which can be further explored for strategic decision-making.

    """)

