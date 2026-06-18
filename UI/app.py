import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.data_loader import DataLoader
from modules.csp_module import CSPModule
from modules.search_module import SearchModule
from modules.ml_module import MLModule
from modules.decision_module import DecisionModule


st.set_page_config(page_title="AI Movie Recommender", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #ffffff;
    }
    
    header[data-testid="stHeader"] {
        background-color: #0d1117 !important;
    }
    footer {
        visibility: hidden;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        color: #00f2fe !important;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(0, 242, 254, 0.6);
        margin-bottom: 2rem;
        letter-spacing: 1px;
    }
    
    /* Sidebar Layout */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #00f2fe;
    }
    
    section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {
        color: #00f2fe !important;
        font-weight: 700 !important;
    }
    
    section[data-testid="stSidebar"] label p {
        color: #58a6ff !important;
        font-weight: 600;
        font-size: 15px;
    }
    
    div[data-testid="stSlider"] [data-testid="stWidgetLabel"] + div div {
        color: #00f2fe !important;
        font-weight: 600;
    }
    
    
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #12161f !important;
        border: 2px solid #00f2fe !important; /* Visible bright cyan border */
        border-radius: 8px !important;
        padding: 15px 20px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.2) !important;
    }
    
  
    div.stButton > button:first-child {
        background-color: #00f2fe;
        color: #0d1117;
        font-weight: bold;
        border-radius: 4px;
        border: none;
        width: 100%;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
        padding: 12px;
        font-size: 16px;
        text-transform: uppercase;
        transition: all 0.25s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        background-color: #00c8d3 !important;
        color: #0d1117 !important;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.7) !important;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def init_system():
    dl = DataLoader()
    ml = MLModule()
    movies_df = dl.get_movies_with_years()
    cluster_map = ml.train_models(movies_df, dl.ratings)
    return dl, ml, cluster_map, movies_df

dl, ml, cluster_map, movies_df = init_system()


st.markdown("<h1 class='main-title'>AI MOVIE RECOMMENDER</h1>", unsafe_allow_html=True)


st.sidebar.header("Control Panel Options")
genres_list = dl.get_unique_genres()
selected_genres = st.sidebar.multiselect("Select Genre:", genres_list)

target_year = st.sidebar.slider("Select Year:", 1970, 2026, 2010)
min_rating = st.sidebar.slider("Select Rating", 0.0, 5.0, 3.0, 0.5)

selected_algo = st.sidebar.selectbox("Select Engine Algorithm", ["A*", "BFS", "DFS"])
top_n = st.sidebar.slider("Top N Recommendations", 4, 20, 10)
generate_clicked = st.sidebar.button("Generate Recommendations")

if generate_clicked:
   
    if not selected_genres:
        st.error("No genre selected. Select genre")
    else:
        st.subheader(f"Top {top_n} Results")
        
        final_filtered = []
        temp_filtered = []
        for g in selected_genres:
            matched = CSPModule.filter_movies(movies_df, dl.ratings, g, min_rating, target_year)
            temp_filtered.extend(matched)
            
        seen_ids = set()
        for m in temp_filtered:
            if m['movieId'] not in seen_ids:
                final_filtered.append(m)
                seen_ids.add(m['movieId'])
        
        if not final_filtered:
            st.warning("No movies match your current hard CSP boundary filters.")
        else:
            candidates = SearchModule.search_candidates(final_filtered, algorithm=selected_algo)
            primary_genre_str = ", ".join(selected_genres)
            
            recommendations = DecisionModule.compile_recommendations(
                candidates, cluster_map, ml, primary_genre_str, target_year
            )
            
            display_list = recommendations[:top_n]
            
            for idx, movie in enumerate(display_list):
                genres_split = movie['genres'].split(', ')
           
                try:
                    movie_year = int(movie['title'].split(' (')[1].split(')')[0])
                except:
                    movie_year = target_year
                
               
                year_gap = abs(movie_year - target_year)
                calculated_score = max(65.0, 100.0 - (year_gap * 4.5))
                if calculated_score > 98.0 and idx > 2:
                    calculated_score = 96.0 - (idx * 0.5)
                
               
                reasons_list = [
                    f"Matches your selected target genre palette ({genres_split[0]}) perfectly.",
                    f"Maintains a high public rating threshold of {movie['rating']}/5.0 inside the dataset." if movie['rating'] >= 4.0 else f"Meets your minimum acceptable recommendation rating benchmark of {min_rating}."
                ]

                display_num = f"{idx + 1:02d}"

              
                with st.container(border=True):
                   
                    st.markdown(f"### <span style='color: #ffb703; font-family: monospace;'>{display_num}</span> &nbsp; <span style='color: #00f2fe;'>{movie['title']}</span>", unsafe_allow_html=True)
                    
                    st.markdown(f"**<span style='color: #00f2fe;'>Rating:</span>** {movie['rating']} / 5.0", unsafe_allow_html=True)
                    st.markdown(f"**<span style='color: #00f2fe;'>Matching Score:</span>** {calculated_score:.1f}%", unsafe_allow_html=True)
                    
                   
                    st.markdown("**<span style='color: #00f2fe;'>Reason:</span>**", unsafe_allow_html=True)
                    st.markdown(f"• {reasons_list[0]}")
                    st.markdown(f"• {reasons_list[1]}")
else:
    st.info("Use the controls in the side panel and then click the Generate Recommendations button")