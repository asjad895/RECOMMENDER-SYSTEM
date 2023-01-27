import streamlit as st

# Create a function to render the home page
def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")

# Create a function to render the about page
def about():
    st.title("About Page")
    st.write("This is the about page.")

# Create a function to render the contact page
def contact():
    st.title("Contact Page")
    st.write("This is the contact page.")

# Create a function to render the navbar
def render_navbar():
    st.markdown(
        """
        <nav>
            <a href="#" onclick="window.home()">Home</a>
            <a href="#" onclick="window.about()">About</a>
            <a href="#" onclick="window.contact()">Contact</a>
        </nav>
        """,
        unsafe_allow_html=True
    )

# Create a function to render the footer
def render_footer():
    st.markdown(
        """
        <footer>
            <p>Copyright © 2021 My Webapp</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

# Create a function to include CSS
def include_css():
    st.markdown(
        """
        <style>
        nav {
            background-color: #303;
            color: #ccc;
            padding: 20px;
        }

        nav a {
            color: #a00;
            text-decoration: none;
            margin-right: 10px;
            text-align: center
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

# Create a function to switch between pages
def switch_page(page):
    if page == "home":
        home()
    elif page == "about":
        about()
    elif page == "contact":
        contact()
    else:
        st.write("Page not found.")

# Main function

def main():
    include_css()
    render_navbar()
    page = st.sidebar.selectbox("Select a page", ["home", "about", "contact"])
    switch_page(page)
    render_footer()

if __name__ == "__main__":
    main()
