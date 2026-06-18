# AI Movie Recommender System

An AI-driven Movie Recommender System that takes user preferences to filter movies using Constraint Satisfaction Problems (CSP) and hybrid search algorithms (A*, BFS, DFS). It uses a machine learning clustering core to analyze data and displays the top recommended movies along with their ratings, matching scores, and reasons for selection.

---

##  Key Features

* **Smart Filtering:** Powered by a Constraint Satisfaction Problem (CSP) module to handle strict user constraints like genres, release years, and minimum ratings.
* **Hybrid Search Core:** Implements A* Search, Breadth-First Search (BFS), and Depth-First Search (DFS) to navigate dataset nodes efficiently.
* **ML Clustering Core:** Groups and analyzes user behavioral metrics to generate accurate profile matching scores.
* **Explainable Recommendations:** Not only recommends movies but also displays exactly why a movie was selected along with its structural score metrics.

---

##  Tech Stack

* **Language:** Python
* **Algorithms:** A* Search, BFS, DFS, Constraint Satisfaction (CSP)
* **Machine Learning:** K-Means Clustering
* **Framework:** Streamlit (for the analytical control dashboard)

---

##  Project Structure

AI_project/
├── UI/
│   └── app.py               # Main interface execution state
├── modules/
│   ├── csp_module.py        # Constraint Satisfaction filters
│   ├── search_module.py     # A*, BFS, and DFS algorithm logic
│   ├── ml_module.py         # Machine learning clustering algorithms
│   └── data_loader.py       # Dataset management pipelines
└── data/
    ├── movies.csv           # Movie catalog data
    └── ratings.csv          # User rating datasets

---

##  How to Run the Project

1. Clone the repository:
   git clone https://github.com/maryamasif1091-cpu/AI_Move_Recommender.git
   cd AI_Move_Recommender

2. Install the required dependencies (pandas, numpy, streamlit, scikit-learn).

3. Run the Streamlit application:
   streamlit run UI/app.py
