import streamlit as st

def show_homepage():
    st.title("Business Intelligence Dashboard")
    st.markdown("""
                This app is designed to provide a comprehensive analysis of transactional data 
                to uncover opportunities that can drive more sales and enhance operational efficiency. 
                Leveraging advanced data analytics, we aim to answer key business questions and generate actionable insights.
    """)

    st.subheader("Visualizations")
    st.markdown("""
                - **Total Revenue**: How much money did we make this year?
                - **Sales Seasonality**: Can we identify any seasonality in the sales?
                - **Product Performance**: What are our best and worst-selling products?
                - **Sales Trends**: How do sales compare to previous months or weeks?
                - **Geographic Distribution**: Which cities are our products delivered to most?
                - **Product Categories**: How do product categories compare in revenue generated and quantities ordered?
                - **Additional Insights**: Discover additional details from data analysis.
    """)

    st.subheader("Steps")
    st.markdown("""
                - **Upload Data**: Load the 2019 transactional dataset into the app.
                - **Data Additions**: You can view and add additional data.
                - **Analysis**: The app provides insights on revenue, seasonality, product performance, and more.
                - **Visualization**: Use interactive charts to explore sales trends and patterns.
                """)

    st.subheader("Benefits of the App")
    st.markdown("""
                - **Sales Optimization**: Identify best-performing products and underperformers.
                - **Efficient Planning**: Recognize trends in customer demand and plan inventory more effectively.
                - **Improved Targeting**: Pinpoint geographical areas with the highest product demand.
                - **Actionable Insights**: Discover potential strategies to increase sales and reduce inefficiencies.
    """)

    st.subheader("Disclaimer")
    st.markdown("""
                Please note that the insights generated depend on the accuracy and completeness of the input data. 
                We recommend considering these findings alongside other business strategies.
    """)

    st.subheader("Contact Us")
    customer_support_email = "kay.yamoah10@gmail.com"
    st.markdown(f"""
    For any questions or further information, feel free to contact us at [this email address]({customer_support_email}).
    """)
