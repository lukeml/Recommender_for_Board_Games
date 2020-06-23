import pickle
import pandas as pd
import numpy as np
from my_functions import top_5_similar_2, game_to_games


# create a function to take in user-entered amounts and apply the model
def get_described(description):

    prediction = top_5_similar_2([description])
    
    return prediction

def get_games(description):

    # make a prediction
    prediction = game_to_games(int(description))
    
    return prediction