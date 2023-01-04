import streamlit as st
import pickle
import pandas as pd
import random
import base64
st.set_page_config(page_title="BOOK RECOMMENDER", page_icon="random", layout="wide", initial_sidebar_state="expanded")

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

st.title('MOVIE RECOMMENDER SYSTEM')

tab1, tab2 = st.tabs(["**WEB APP FOR MOVIE RECOMMENDATION**", "**ABOUT**"])
def random_emoji():
    st.session_state.emoji = random.choice(emojis)
    # initialize emoji as a Session State variable


if "emoji" not in st.session_state:
    st.session_state.emoji = "👈"


emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]
def recommend(sel_movie):
    ind = movies[movies['title'] == sel_movie].index[0]
    sim = similarity[ind]
    top_five_movie = sorted(list(enumerate(sim)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie=[]
    for j in top_five_movie:
        recommended_movie.append(movies.iloc[j[0]].title)
    return recommended_movie


with tab1:
    st.markdown("This web app is recommendation of movie where u can gives movie name and enjoy your favourite choice!")
    st.header("Select Movie Name")
    selected_movie=st.selectbox('Choose your movie', movies['title'])
    # if st.button(f"RECOMMEND {st.session_state.emoji}", on_click=random_emoji):
    if st.button("RECOMMEND"):
        st.balloons()
        recom_m=recommend(selected_movie)
        for i in recom_m:
            st.success(i)


with tab2:
    st.markdown("This is based on the algorithm of content based similarity for recommendation in machine learning")
    st.markdown("You can check it on [my Github](https://github.com/asjad895?tab=repositories) in Recommender system repo")
    st.caption("___________________________________________________________________________________________________")
