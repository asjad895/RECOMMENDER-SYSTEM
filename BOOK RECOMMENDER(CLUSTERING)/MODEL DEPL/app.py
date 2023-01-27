import streamlit as st
import pickle
import numpy as np

import random
import base64
st.set_page_config(page_title="BOOK RECOMMENDER", page_icon="random", layout="wide", initial_sidebar_state="expanded")
# navbar = st.container()
# navbar.markdown("""
#     <style>
#         .navbar {
#             background-color: #f8f9fa;
#             padding: 10px;
#             text-align: center;
#         }
#         .navbar a {
#             margin: 0 20px;
#             text-decoration: none;
#             color: #000;
#         }
#     </style>
# """, unsafe_allow_html=True)
# navbar.markdown("<div class='navbar'>")
# navbar.markdown("<a href='#'>Home</a>")
# navbar.markdown("<a href='#'>About</a>")
# navbar.markdown("<a href='#'>Contact</a>")
# navbar.markdown("</div>")
st.markdown(
    """
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>
    """,
    unsafe_allow_html=True
)
st.markdown("""<style>
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
</style>)""")

def add_bg_from_local(image_file):
    path=image_file
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        st.markdown(
             f"""
             <style>.stApp {{background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
             background-size: cover}}             </style>""", unsafe_allow_html=True
        )


book_pivot=pickle.load(open('book_pivot.pkl', 'rb'))
model=pickle.load(open('nn_model.pkl', 'rb'))
title=pickle.load(open('title.pkl', 'rb'))

st.title('BOOKS RECOMMENDER SYSTEM')

tab1, tab2 = st.tabs(["**WEB APP FOR BOOK RECOMMENDATION**", "**ABOUT**"])
def random_emoji():
    st.session_state.emoji = random.choice(emojis)
    # initialize emoji as a Session State variable


if "emoji" not in st.session_state:
    st.session_state.emoji = "👈"


emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]
def recommend(book):
    ind=np.where(book_pivot.index==book)[0][0]
    distances, suggestion=model.kneighbors(book_pivot.iloc[ind, :].values.reshape(1, -1), n_neighbors=6)
    rec_book=[]
    for j in range((len(suggestion))):
        rec_book.append(book_pivot.index[suggestion[j]])
    return rec_book


with tab1:
    st.markdown("This web app is recommendation of book where u can gives book name and enjoy your favourite choice!")
    st.header("Select Book Name")
    selected_book=st.selectbox('Choose your book', title)
    # if st.button(f"RECOMMEND {st.session_state.emoji}", on_click=random_emoji):
    if st.button("RECOMMEND"):
        st.balloons()
        recom_m=recommend(selected_book)
        for i in range(1, 6):
            st.success(recom_m[0][i])


with tab2:
    st.markdown("This is based on the algorithm of clustering using knn for recommendation in machine learning")
    st.markdown("You can check it on [my Github](https://github.com/asjad895?tab=repositories) in Recommender system repo")
    st.caption("___________________________________________________________________________________________________")
