import streamlit as st
import pickle as pk
import sys
import os
import requests
from src.utils import Recommendation
from src.exception import CustomException
import time


def load_data():
    movies_path = 'Artifacts/movie_list.pkl'
    similarity_path = 'Artifacts/similarity.pkl'
    
    try:
        with open(movies_path, 'rb') as file:
            st.session_state.movies = pk.load(file)
        with open(similarity_path, 'rb') as file:
            st.session_state.similarity = pk.load(file)
        st.session_state.data_loaded = True
        print("Data loaded successfully.")
    except Exception as e:
        raise CustomException(e, sys)
    
if 'data_loaded' not in st.session_state:
    load_data()

movie_list = st.session_state.movies['title']

def get_poster(movieid, retries=3, delay=1, backoff=2):
    posters = []
    for i in movieid:
        url = f"https://api.themoviedb.org/3/movie/{i}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        for attempt in range(retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                poster_path = data.get('poster_path')
                if poster_path:
                    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
                    posters.append(full_path)
                else:
                    posters.append(None)
                break
            except requests.exceptions.RequestException as e:
                print(f"Error fetching poster for movie {i}: {e}")
                time.sleep(delay * (backoff ** attempt))
                continue
    return posters

st.markdown(
    """
    <style>
    .movie-title {
        white-space: normal;
        word-wrap: break-word;
        text-align: center;
        height: 60px; /* Fixed height for movie titles */
        overflow: hidden; /* Hide overflow */
    }
    .movie-poster {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Movie Recommendation System")
selected_movie = st.selectbox(
    'Type the movie name',
    movie_list
)

obj = Recommendation()

if st.button('Show Recommendation'):
    movie_id, movie_name = obj.recommend(selected_movie, st.session_state.similarity, st.session_state.movies)
    movie_poster = get_poster(movie_id)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"<div class='movie-title'>{movie_name[i]}</div>", unsafe_allow_html=True)
            st.image(movie_poster[i])
    print("Successfully fetched all")
    
