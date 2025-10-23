import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from PIL import Image

# Load the model and data
with open('netflix_recommendation_model.pkl', 'rb') as file:
    data = pickle.load(file)
    cosine_sim = data['cosine_sim']
    cosine_sim2 = data['cosine_sim2']
    indices = data['indices']
    netflix_dataset = data['netflix_dataset']

# Function to get recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    title = title.lower().strip()
    if title not in indices:
        return ["Movie not found in dataset"]
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return netflix_dataset['title'].iloc[movie_indices]

def get_recommendations_new(title, cosine_sim=cosine_sim2):
    title = title.lower().strip()
    if title not in indices:
        return ["Movie not found in dataset"]
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return netflix_dataset['title'].iloc[movie_indices]

# Streamlit App
st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon=":clapper:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Home", "Recommendations"]
page = st.sidebar.radio("Go to", pages)

# Home Page
if page == "Home":
    st.title("Netflix Recommendation System")
    st.write("## About")
    st.write(
        """
        Welcome to the Netflix Recommendation System! This web application uses advanced machine learning algorithms to provide personalized recommendations for Netflix movies and TV shows. 
        Explore the recommendations and discover content that suits your preferences.
        """
    )
    netflix_image = Image.open("netflix_image.jpg")
    st.image(netflix_image, caption="Netflix", use_column_width=True)

# Recommendation Page
elif page == "Recommendations":
    st.title("Get Your Netflix Recommendations")
    
    # Input for movie title
    movie_title = st.text_input("Enter a movie title for recommendations")

    # Recommendation Type
    recommendation_type = st.radio(
        "Recommendation Type",
        ('Content-Based', 'Hybrid')
    )

    # Display recommendations
    if st.button("Get Recommendations"):
        if movie_title:
            try:
                if recommendation_type == 'Content-Based':
                    recommendations = get_recommendations(movie_title)
                else:
                    recommendations = get_recommendations_new(movie_title)
                st.write(f"Recommendations for {movie_title}:")
                for idx, title in enumerate(recommendations, 1):
                    st.write(f"{idx}. {title}")
            except KeyError:
                st.write("Sorry, the movie title you entered is not in our database. Please try another title.")
        else:
            st.write("Please enter a movie title.")
