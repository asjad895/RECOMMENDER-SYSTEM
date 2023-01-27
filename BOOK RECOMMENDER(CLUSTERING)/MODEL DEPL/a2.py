import streamlit as st

# Create a function for the Home page
def home():
    st.title("Home")
    st.write("Welcome to the home page.")

# Create a function for the About page
def about():
    st.title("About")
    st.write("This is an example webapp using Streamlit.")

# Create a function for the Contact page
def contact():
    st.title("Contact")
    st.write("You can contact us at example@email.com.")

# Create a function for the navbar
def navbar():
    st.markdown(
        """
        <nav>
            <a href='/'>Home</a>
            <a href='/about'>About</a>
            <a href='/contact'>Contact</a>
        </nav>
        """,
        unsafe_allow_html=True
    )

# Create a function for the footer
def footer():
    st.markdown(
        """
        <footer>
            <p>Copyright © 2021 My Webapp</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

# Create a function to add CSS to the app
def add_css():
    st.markdown(
        """
        <style>
        nav {
            background-color: #333;
            color: #fff;
            padding: 10px;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin-right: 10px;
        }

        footer {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Create a function to handle the routing
def routing():
    add_css()
    navbar()


if __name__ == "__main__":
    routing()
