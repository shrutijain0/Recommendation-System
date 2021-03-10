# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:15:06 2021

@author: milin
"""

import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist,squareform
movie_df=pd.read_csv('movies.csv')
rating_df=pd.read_csv('ratings.csv')
# Content Based Recommendation system.

df = pd.merge(rating_df,movie_df,on='movieId')

# removed the other genres and only took the first genres for every movie
movie_df['genres'] = movie_df['genres'].apply(lambda x: x.split('|')[0])

# made a cross table of movie title and there genres.
movie_crosstab=pd.crosstab(movie_df['title'],movie_df['genres'])

# using pdist to find distance
jaccard_distance=pdist(movie_crosstab,metric="jaccard")

# we need opposite of distance which is similarity so we are going to subtracrt all dist value with 1.
jaccard_similarity=1.0-squareform(jaccard_distance)

similarity_df=pd.DataFrame(jaccard_similarity,index=movie_crosstab.index,columns=movie_crosstab.index)

#lets make recommendation
similarity_series=similarity_df.loc['Jumanji (1995)']
ordered_similarity=similarity_series.sort_values(ascending=False)
print(ordered_similarity)


