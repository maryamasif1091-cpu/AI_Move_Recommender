import queue

class SearchModule:
    """
    Simulates traversing a state-space network of candidate movies.
    """
    @staticmethod
    def search_candidates(movie_list, algorithm="A*"):
        if not movie_list:
            return []
            
       
        if algorithm == "BFS":
            # Level-order queue processing
            q = queue.Queue()
            for m in movie_list: q.put(m)
            result = []
            while not q.empty():
                result.append(q.get())
            return result
            
        elif algorithm == "DFS":
           
            stack = list(movie_list)
            result = []
            while stack:
                result.append(stack.pop())
            return result
            
        elif algorithm == "A*":
           
            sorted_list = sorted(movie_list, key=lambda x: x.get('avg_rating', 0), reverse=True)
            return sorted_list
            
        return movie_list