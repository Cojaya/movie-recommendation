import pickle
import numpy as np
import pandas as pd
import streamlit as st

ipc = pickle.load(open("piple.pkl", "rb"))
df = pd.read_csv("datasets/IMDB-Movie-Data.csv")


titles = df['Title'].to_list()

def get_index_from_name(name):
    return df[df['Title'] == name].index[0]

def recommend_movie(movie_name,k=8):
    idx = get_index_from_name(movie_name)

    sim_scores = list(enumerate(ipc[idx]))
    sim_scores.sort(key=lambda x: x[1],reverse=True) 
    movie_indices = [i[0] for i in sim_scores] 
    list1 = df.iloc[movie_indices]['Title'].head(k).to_list()
    for i in list1[1:]:
        yield i


st.title('Movie Recommendation')

movie = st.selectbox(label="Select movies",options=titles)
slider_count = st.slider(label="movie_conut",min_value=5,max_value=10)

btn = st.button('Submit')
if btn:
    for value in recommend_movie(movie,slider_count+1):
        st.header(value)

btn2 = st.button('Get Details')
if btn2:
    idx = get_index_from_name(movie)
    st.text(df.iloc[idx])