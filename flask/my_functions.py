import pandas as pd
import numpy as np

import re
import string

from sklearn.metrics import pairwise_distances
from pipeline import NLPProcessor
from gensim.parsing.preprocessing import STOPWORDS

import pickle

my_model = pickle.load(open("nmf_model_15_21May.pickle", "rb"))
my_doc_topic = pickle.load(open("doc_topic_nmf_15_21May.pickle", "rb"))
nlp1 = pickle.load(open("nlp1_15_21May.pickle", "rb"))
df_reviews = pickle.load(open("df_reviews_21May.pickle", "rb"))
df_reviews['game_link'] = df_reviews[['game', 'url']].apply(lambda x: '<a href="{}">{}</a>'.format(x[1], x[0]), axis=1)


def top_5_similar_2(list_string, my_nlp=nlp1, model_type=my_model, doc_topic=my_doc_topic):
    """
    Given a list containing a string, print the top 5 games based on cosine distance 
    
    Input:
            list_string is a list with a string 
            my_nlp is the nlp model used to vectorize and tokenize the original text data 
            doc_topic, numpy array, is array with games as rows, topic contribution as columns
            model_type is the model used to create the sparse topic array

    """
    vec = my_nlp.transform(list_string)
    vtrans = model_type.transform(vec)
    array_5 = pairwise_distances(vtrans, doc_topic, metric='cosine').argsort()[0][0:5]
    # result_df = df_reviews[['game_link']].iloc[array_5]
    return df_reviews[['game']].iloc[array_5]
    # return("test")
    return result_df


def game_to_games(game_index, doc_topic=my_doc_topic, n_games=5):
    """
    
    Given a game index (from the dataframe), print the top n games by cosine distance

    Input:
            game_index, int, is index of row associated with game
            doc_topic, numpy array, is array with games as rows, topic contribution as columns
            n_games, int, is number of games to return that are most similar

    """
    my_array = pairwise_distances(doc_topic[game_index].reshape(1, -1), doc_topic, metric='cosine').argsort()[0][
               :n_games + 1]
    #     print(df_reviews[['game', 'description']].iloc[my_array])
    return df_reviews[['game']].iloc[my_array]
