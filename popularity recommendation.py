# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:02:48 2021

@author: milin
"""
# Recommendation system using movie lens data set.

import pandas as pd
import numpy as np

movie_df=pd.read_csv('movies.csv')
rating_df=pd.read_csv('ratings.csv')

df = pd.merge(rating_df,movie_df,on='movieId')

# taking movie rating which has been reviwed by more than 50 people.
popularity=df['title'].value_counts()
popular_movies=popularity[popularity>50].index

# placing all pouplar movie in original data set
movie_ranking=df[df['title'].isin (popular_movies)]

# took the average rating and sorted the value in descending order to get most popular recommendation movies.
avg_ranking=movie_ranking[['title','rating']].groupby('title').mean()
popular_recommendation=avg_ranking.sort_values(by='rating',ascending=False)

popular_recommendation.head()
