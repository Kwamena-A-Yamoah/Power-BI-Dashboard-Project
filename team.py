import streamlit as st
from PIL import Image

def meet_the_team():
    st.title("Meet the Team")
    st.write("Get to know the brilliant minds behind this dashboard project!")

    # Function to create a team member card
    def team_member_card(name, role, bio, image_path):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(image_path, width=150)
        with col2:
            st.subheader(name)
            st.write(f"{role}")
            st.write(bio)
        st.markdown("---")

    # Team member 1
    team_member_card(
        "Brian Siaw",
        "Data Scientist",
        "Brian is passionate about turning data into actionable insights. With a background in statistics and machine learning, he leads our data analysis efforts.",
        "photos/brian.jpg"
    )

    # Team member 2
    team_member_card(
        "Saskia Byanca Njoki",
        "Power BI Specialist",
        "Saskia excels in Power BI, transforming complex data into interactive dashboards that drive data-informed decisions.",
        "photos/saskia.jpg"
    )

    # Team member 3
    team_member_card(
        "Kwamena Afful Yamoah",
        "Full Stack Developer",
        "Kwamena builds fully integrated web apps, ensuring our dashboard is both functional and user-friendly with seamless front-end and back-end integration.",
        "photos/kay.jpg"
    )

    # Add more team members as needed

    st.write("## Our Mission")
    st.write("Our team is dedicated to leveraging data analytics to drive business success. We believe in the power of data-driven decision making and strive to provide clear, actionable insights through our dashboard.")

    st.write("## Contact Us")
    st.write("Have questions or feedback? We'd love to hear from you!")
    st.write("📧 Email: team@dashboard.com")
    st.write("📞 Phone: (123) 000-0000")

