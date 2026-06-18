class DecisionModule:
    """
    Consolidates the output matrices of your heuristics and predictive models.
    """
    @staticmethod
    def compile_recommendations(candidates, cluster_map, ml_module, target_genre, target_year):
        final_list = []
        
        for movie in candidates:
            m_id = movie['movieId']
            cluster_id = cluster_map.get(m_id, 0)
            
            # Predict user engagement rating via trained ANN
            predicted_rating = ml_module.predict_rating(movie['year'], cluster_id)
            
            # Calculate programmatic match percentage
            from modules.heuristic_module import HeuristicModule
            match_score = HeuristicModule.compute_match_score(movie, target_genre, target_year)
            
            # Build structured explanations
            explanation = f"This {movie['year']} film fits your target timeframe and matches your preference for {target_genre} profiles."
            
            final_list.append({
                'title': movie['title'],
                'rating': movie['avg_rating'],
                'predicted_rating': predicted_rating,
                'match_score': match_score,
                'genres': movie['genres'].replace('|', ', '),
                'explanation': explanation
            })
            
        # Sort by final heuristic match calculations
        final_list = sorted(final_list, key=lambda x: x['match_score'], reverse=True)
        return final_list