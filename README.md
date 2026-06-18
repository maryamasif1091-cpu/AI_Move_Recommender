# AI Movie Recommender System

An intelligent movie recommendation system that combines Artificial Intelligence, Constraint Satisfaction Problems (CSP), search algorithms, and machine learning techniques to deliver personalized movie suggestions. The system analyzes user preferences, applies constraint-based filtering, explores recommendation paths using hybrid search strategies, and presents the most relevant movies with ratings, matching scores, and explainable insights

---

##  Key Features

* Filters movies based on user-defined constraints such as genre, release year, and minimum rating.
* Uses Constraint Satisfaction Problem (CSP) techniques to ensure recommendations satisfy all specified preferences.
* Implements A*, Breadth-First Search (BFS), and Depth-First Search (DFS) for efficient dataset exploration.
* Applies K-Means Clustering to identify user behavior patterns and improve recommendation accuracy.
* Generates personalized movie recommendations with profile matching scores.
* Provides movie ratings alongside recommendation results.
* Explains why each movie was selected to enhance transparency and user trust.
* Offers an interactive analytical dashboard built with Streamlit.
* Combines AI, search algorithms, and machine learning in a unified recommendation pipeline.
  
---

##  Tech Stack

* **Language:** Python
* **Algorithms:** A* Search, BFS, DFS, Constraint Satisfaction (CSP)
* **Machine Learning:** K-Means Clustering
* **Framework:** Streamlit (for the analytical control dashboard)

---


##  How to Run the Project

1. Clone the repository:
   git clone https://github.com/maryamasif1091-cpu/AI_Move_Recommender.git
   cd AI_Move_Recommender

2. Install the required dependencies (pandas, numpy, streamlit, scikit-learn).

3. Run the Streamlit application:
   streamlit run UI/app.py
