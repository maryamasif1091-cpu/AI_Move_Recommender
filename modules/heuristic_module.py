class HeuristicModule:
    """
    Evaluates and ranks candidate movies using a structural matching weight function.
    """
    @staticmethod
    def compute_match_score(movie, target_genre, target_year):
      
        score = 50.0
        
        # Genre bonus (h(n))
        if target_genre in movie['genres'].split('|'):
            score += 25.0
       
        year_diff = abs(movie['year'] - target_year)
        if year_diff == 0:
            score += 25.0
        elif year_diff <= 3:
            score += 15.0
        elif year_diff <= 7:
            score += 5.0
            
        return min(100.0, score)