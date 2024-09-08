import streamlit as st
import login            # Import the login module
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
       
       # ================================================================= 
        # Navigation menu
        # st.sidebar.title('Navigation')
        # st.session_state.page = st.sidebar.radio('Select Page', ['Home', 'Dashboard', 'Contacts'])

        # # Render the selected page
        # if st.session_state.page == 'Home':
        #     st.title('Home')
        #     st.write('Welcome to the home page!')
        # elif st.session_state.page == 'Dashboard':
        #     st.title('Dashboard')
        #     st.write('Welcome to the dashboard page!')
        # elif st.session_state.page == 'Contacts':
        #     st.title('Contacts')
        #     st.write('Welcome to the contacts page!')
      
# =================================================================  This next one has better style
        # Navigation menu
        with st.sidebar:
            st.sidebar.title('Navigation')
            selected = option_menu(
                menu_title=None,  # No title for the sidebar menu
                options=["Home", "Dashboard", "Contacts"],  # Pages
                icons=["house", "bar-chart", "envelope"],  # Optional icons for each page
                menu_icon="cast",  # Optional icon for the menu
                default_index=0,  # Home is selected by default
            )

        # Render the selected page
        if selected == "Home":
            st.title('Home')
            st.write('Welcome to the home page!')
        elif selected == "Dashboard":
            st.title('Dashboard')
            st.write('Welcome to the dashboard page!')
        elif selected == "Contacts":
            st.title('Contacts')
            st.write('Welcome to the contacts page!')
# =================================================================
        
    else:
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