class CSPModule:
    """
    Hard-filtering based on user-defined constraints.
    Returns only the movies that satisfy all criteria.
    """
    @staticmethod
    def filter_movies(movies_df, ratings_df, selected_genre, min_rating, target_year):
        # Calculate average rating per movie to filter on
        avg_ratings = ratings_df.groupby('movieId')['rating'].mean().to_dict()
        
        filtered_movies = []
        
        for _, movie in movies_df.iterrows():
            # 1. Genre Constraint
            if selected_genre and selected_genre != "All":
                if selected_genre not in movie['genres'].split('|'):
                    continue
            
            # 2. Rating Constraint
            m_id = movie['movieId']
            movie_avg_rating = avg_ratings.get(m_id, 0.0)
            if movie_avg_rating < min_rating:
                continue
                
            # 3. Year Constraint (Filter within ±7 years of choice for a flexible CSP match)
            if abs(movie['year'] - target_year) > 7:
                continue
                
            # Satisfies all constraints
            movie_copy = movie.to_dict()
            movie_copy['avg_rating'] = round(movie_avg_rating, 2)
            filtered_movies.append(movie_copy)
            
        return filtered_movies