import streamlit as st
import pickle as pk
import sys
import os
import requests
import time
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pt = PorterStemmer()
cv=CountVectorizer(max_features=5000, stop_words='english')

MOVIE_LIST_URL = "https://drive.google.com/uc?export=download&id=1uBgqLmgibehSLWi6vNJ7Ydm8bo-4ZLo9"
SIMILARITY_URL = "https://www.dropbox.com/scl/fi/d55bf7gj87wka9mr16ln0/similarity.pkl?rlkey=alu41tgjd89xhc0n8iic15l6j&st=r5f883im&dl=1"
LOCAL_MOVIES_PATH = 'Artifacts/movie_list.pkl'
LOCAL_SIMILARITY_PATH = 'Artifacts/similarity.pkl'

def load_data():
    try:
        # Check if local files exist
        if not os.path.exists(LOCAL_MOVIES_PATH) or not os.path.exists(LOCAL_SIMILARITY_PATH):
            print("Local files not found. Attempting to download from cloud.")
            download_from_cloud()
        
        # Load data from local files
        with open(LOCAL_MOVIES_PATH, 'rb') as file:
            st.session_state.movies = pk.load(file)
        with open(LOCAL_SIMILARITY_PATH, 'rb') as file:
            st.session_state.similarity = pk.load(file)
        
        st.session_state.data_loaded = True
        print("Data loaded successfully from local files.")
    
    except Exception as e:
        print("Error loading data from local files. Attempting to download from cloud.")

def stemming(text):
    l=[]
    for i in text.split():
        l.append(pt.stem(i))
    return " ".join(l)

def download_from_cloud():
    try:
        # Download movies_list.pkl
        print("Initiated download")
        with requests.get(f"{MOVIE_LIST_URL}") as response1:
            response1.raise_for_status()
            st.session_state.movies = pk.loads(response1.content)
            print("Movies downloaded")
            st.session_state.movies['tag'] = st.session_state.movies['tag'].apply(stemming)
            vector = cv.fit_transform(st.session_state.movies['tag']).toarray()
            st.session_state.similarity = cosine_similarity(vector)
            print("Similarity downloaded")
            with open(LOCAL_MOVIES_PATH, 'wb') as file1:
                file1.write(response1.content)
        
        
        print("Downloaded data successfully from cloud storage.")
    
    except requests.exceptions.RequestException as e:
        print("Error downloading data from cloud storage.")


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

def recommend(movie, similarity, df):
    try:
        index = df[df['title']==movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
        movie_name = []
        movie_id = []
        for i in distances[1:6]:
            movie_name.append(df.iloc[i[0]].title)
            movie_id.append(df.iloc[i[0]].id)
        return movie_id, movie_name
    except Exception as e:
        print("Error recommending movie")

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

st.header("Movie Recommendation System\n(Content Based)")
selected_movie = st.selectbox(
    'Type the movie name',
    movie_list
)

if st.button('Show Recommendation'):
    movie_id, movie_name = recommend(selected_movie, st.session_state.similarity, st.session_state.movies)
    movie_poster = get_poster(movie_id)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"<div class='movie-title'>{movie_name[i]}</div>", unsafe_allow_html=True)
            st.image(movie_poster[i])
    print("Successfully fetched all")
    
