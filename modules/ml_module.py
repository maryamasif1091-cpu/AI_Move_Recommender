import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPRegressor

class MLModule:
    def __init__(self):
        self.kmeans = None
        self.ann = None
        
    def train_models(self, movies_df, ratings_df):
        # 1. Simple K-Means Clustering based on unique movie features (Year, Avg Rating)
        avg_ratings = ratings_df.groupby('movieId')['rating'].mean().reset_index()
        features = movies_df.merge(avg_ratings, on='movieId', how='left').fillna(3.0)
        
        X_cluster = features[['year', 'rating']].values
        n_clusters = min(3, len(X_cluster))
        if n_clusters > 1:
            self.kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
            features['cluster'] = self.kmeans.fit_predict(X_cluster)
        else:
            features['cluster'] = 0
            
        # 2. Simple Neural Network (MLPRegressor) to predict rating based on Year and Cluster
        X_train = features[['year', 'cluster']].values
        y_train = features['rating'].values
        
        self.ann = MLPRegressor(hidden_layer_sizes=(8, 4), max_iter=500, random_state=42)
        self.ann.fit(X_train, y_train)
        
        return features.set_index('movieId')['cluster'].to_dict()

    def predict_rating(self, year, cluster_id):
        if self.ann is None:
            return 3.5
        pred = self.ann.predict([[year, cluster_id]])[0]
        return round(float(np.clip(pred, 1.0, 5.0)), 1)