import streamlit as st
import login            # Import the login module
import data, home, dashboard, team
from streamlit_option_menu import option_menu


# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
    
# Define a function to handle the login state
def check_authentication():
    return st.session_state.get('authenticated', False)

# Logout function
def logout():
    st.session_state['authenticated'] = False
    st.session_state.pop('username', None)
    st.session_state['page'] = 'Login'          # Set the page to Login
    
def main():
    if check_authentication():
        if 'page' not in st.session_state:
            st.session_state['page'] = 'Home'
        
        # Sidebar with logout option
        st.sidebar.title(f"Welcome, {st.session_state['username'].title()}")
        if st.sidebar.button('Logout'):
            logout()
            
# =================================================================  This next one has better style

        # Navigation menu
        with st.sidebar:
            
            selected = option_menu(
                menu_title='Main Menu',  # No title for the sidebar menu
                menu_icon="arrow",  # Optional icon for the menu
                options=["Home", "Data", "Dashboard", "Team"],  # Pages
                icons=["house", "file-text", "bar-chart"],  # Optional icons for each page
                default_index=0,  # Home is selected by default
                orientation= "vertical", 
            )


        # Render the selected page
        if selected == "Home":
            st.title('Home')
            st.write('Welcome to the home page!')
            home.show_homepage()
        elif selected == "Dashboard":
            st.title('Sales Dashboard')
            #st.write('Welcome to the dashboard page!')
            dashboard.show_dashboard()
        elif selected == "Data":
            st.write('Welcome to the data page!')
            data.show_data()
        elif selected == "Team":
            team.meet_the_team()
            
# =================================================================
        
    else:
        # sidebar logo
        st.sidebar.image('logos/logo-no-background.png', caption='Online Analytics', use_column_width=True)
            
        # Show the login form in the sidebar if not authenticated
        login.show_login()
        
        page_bg_img = '''
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/185576/pexels-photo-185576.jpeg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        </style>
        '''

        # Display the background image
        st.markdown(page_bg_img, unsafe_allow_html=True)

if __name__ == "__main__":
    main()