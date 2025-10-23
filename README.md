🎬 Netflix Hybrid Recommendation System
📘 Overview

This project presents a hybrid recommendation system for Netflix that combines content-based filtering and collaborative filtering to deliver accurate, personalized, and diverse recommendations. The system integrates TF-IDF vectorization and cosine similarity to identify content similarity based on multiple features such as title, cast, director, genre, and description.

The hybrid model effectively addresses key challenges in recommendation systems such as the cold start problem and feedback loop bias. An intuitive Streamlit web application is built to allow users to easily input a movie or TV show title and instantly receive recommendations.

🚀 Key Features

Hybrid Recommendation Approach: Combines the strengths of collaborative and content-based filtering.

TF-IDF and Cosine Similarity: Used for computing similarity scores between items.

Multi-Feature Integration: Utilizes metadata like cast, director, genre, and description for better accuracy.

Interactive Web Interface: Developed using Streamlit for real-time recommendations.

Data-Driven Insights: Includes exploratory data analysis (EDA) on Netflix content trends.

Cold Start Handling: Mitigates issues for new users or new content through hybrid strategy.

🧠 Project Structure
📂 Netflix-Recommendation-System
│
├── 📄 netflix_dataset.csv                 # Main Netflix dataset
├── 📄 IMDb movies.csv                     # IMDb metadata file
├── 📄 IMDb ratings.csv                    # IMDb ratings data
├── 📄 netflix_recommendation_model.pkl    # Saved model (pickle file)
│
├── 📜 netflix_recommendation.ipynb        # Data preprocessing, EDA, model creation
├── 📜 app.py                              # Streamlit web application script
│
├── 🖼️ netflix_image.jpg                   # Image displayed in the web app
├── 📘 README.md                           # Project documentation
└── 📄 requirements.txt                    # List of libraries/dependencies

🧩 Technologies and Libraries Used
Category	Library / Tool	Purpose
Data Handling	pandas, numpy	Data preprocessing and manipulation
Visualization	matplotlib, seaborn	Data exploration and visual analysis
NLP / ML	scikit-learn	TF-IDF, CountVectorizer, cosine similarity
Web App	streamlit	Building the interactive UI
Image Processing	PIL	Displaying images in the Streamlit app
Model Storage	pickle	Saving and loading trained model
Miscellaneous	warnings	Suppressing unnecessary alerts
⚙️ Installation and Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/netflix-hybrid-recommendation.git
cd netflix-hybrid-recommendation

2️⃣ Create and Activate a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Project
Step 1: Train/Prepare the Model

If you wish to re-run the model training:

python netflix_recommendation.ipynb


This will generate the netflix_recommendation_model.pkl file.

Step 2: Launch the Streamlit Application
streamlit run app.py

Step 3: Use the App

Enter a movie or TV show title in the input box.

Choose between Content-Based or Hybrid recommendation.

Click “Get Recommendations” to see top similar titles.

📊 Example Outputs

Content-Based Example:
Input: Black Panther
Output:

John Henry

The Writer

Daughters of the Dust

Naruto Shippûden: The Will of Fire

Transformers Prime

Hybrid Example:
Input: Welcome
Output:

Tees Maar Khan

The Shaukeens

Phir Hera Pheri

Humko Deewana Kar Gaye

Race

💡 Learning Outcomes

Through this project, the following concepts and skills were gained:

Application of machine learning algorithms in recommendation systems.

Feature extraction using TF-IDF and CountVectorizer.

Model integration using cosine similarity for item comparison.

Data visualization and exploratory analysis for insight generation.

Web deployment with Streamlit for interactive applications.

🧭 Future Enhancements

Integrate user-based collaborative filtering with implicit feedback.

Add genre-based clustering using unsupervised learning.

Implement deep learning models (e.g., autoencoders, neural CF).

Incorporate real-time user feedback for adaptive recommendations.
