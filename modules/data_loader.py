import pandas as pd
import numpy as np
import os

class DataLoader:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        self.movies = None
        self.ratings = None
        self.tags = None
        self.load_data()

    def load_data(self):
        # Fallback to creating mock data if files don't exist yet
        try:
            self.movies = pd.read_csv(os.path.join(self.data_dir, 'movies.csv'))
            self.ratings = pd.read_csv(os.path.join(self.data_dir, 'ratings.csv'))
            self.tags = pd.read_csv(os.path.join(self.data_dir, 'tags.csv'))
        except Exception:
            # Create a robust mock dataset so the app works instantly out-of-the-box
            print("CSV files not found. Generating sample data...")
            os.makedirs(self.data_dir, exist_ok=True)
            
            # Mock Movies
            genres_list = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Thriller', 'Romance', 'Horror']
            movie_data = []
            np.random.seed(42)
            titles = [
                "The Matrix (1999)", "Inception (2010)", "Interstellar (2014)", 
                "The Dark Knight (2008)", "Superbad (2007)", "The Hangover (2009)", 
                "Pulp Fiction (1994)", "Forrest Gump (1994)", "The Godfather (1972)",
                "Spirited Away (2001)", "Parasite (2019)", "Get Out (2017)"
            ]
            for i, title in enumerate(titles):
                g = np.random.choice(genres_list, size=np.random.randint(1, 3), replace=False)
                movie_data.append({
                    'movieId': i + 1,
                    'title': title,
                    'genres': '|'.join(g)
                })
            self.movies = pd.DataFrame(movie_data)
            self.movies.to_csv(os.path.join(self.data_dir, 'movies.csv'), index=False)
            
            # Mock Ratings
            user_ids = np.repeat(np.arange(1, 11), 5)
            movie_ids = np.random.choice(self.movies['movieId'].values, size=50)
            ratings_val = np.random.choice([3.0, 3.5, 4.0, 4.5, 5.0], size=50)
            self.ratings = pd.DataFrame({
                'userId': user_ids,
                'movieId': movie_ids,
                'rating': ratings_val,
                'timestamp': 1234567890
            })
            self.ratings.to_csv(os.path.join(self.data_dir, 'ratings.csv'), index=False)
            
            # Mock Tags
            self.tags = pd.DataFrame({
                'userId': [1, 2, 3],
                'movieId': [1, 2, 3],
                'tag': ['masterpiece', 'mind-bending', 'classic'],
                'timestamp': 1234567890
            })
            self.tags.to_csv(os.path.join(self.data_dir, 'tags.csv'), index=False)

    def get_unique_genres(self):
        genres = set()
        for g_str in self.movies['genres'].dropna():
            for g in g_str.split('|'):
                genres.add(g)
        return sorted(list(genres))

    def extract_year(self, title):
        import re
        match = re.search(r'\((\d{4})\)', title)
        return int(match.group(1)) if match else None

    def get_movies_with_years(self):
        df = self.movies.copy()
        df['year'] = df['title'].apply(self.extract_year)
        # fill missing years with a default
        df['year'] = df['year'].fillna(2000).astype(int)
        return df