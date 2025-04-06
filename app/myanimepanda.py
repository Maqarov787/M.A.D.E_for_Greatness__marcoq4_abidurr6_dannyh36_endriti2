import pandas as pd
import re
anime = pd.read_csv("static/anime.csv")

#Mutator methods
def keep():
    dropped_anime = anime[anime["popularity"] > 1000].index
    anime.drop(dropped_anime, inplace=True)

def remove_nsfw():
    nsfw_anime = anime[anime["nsfw"] != "white"].index
    anime.drop(nsfw_anime, inplace=True)

def filter_chars():
#Will filter out special characters in any of the data.
#Warning: Consulted with the AI overlords (GPT-4o) to construct this method. The prompt given was "how would I filter out rows of data in python pandas that contain non-ascii characters?"
    global anime
    anime = anime[anime["title"].apply(lambda x: x.isascii())]

def drop_columns():
    anime.drop(["id", "created_at", "updated_at", "alternative_titles_en", "alternative_titles_ja", "alternative_titles_synonyms"], axis=1, inplace=True)

def remove_zero_mean():
    zero_values = anime[anime["mean"] == 0].index
    anime.drop(zero_values, inplace=True)

def remove_zero_popularity():
    zero_values = anime[anime["popularity"] == 0].index
    anime.drop(zero_values, inplace=True)

def sort():
    anime.sort_values(by=["popularity"], inplace=True)

def valid_data():
    remove_zero_mean()
    remove_zero_popularity()
    drop_columns()
    remove_nsfw()
    filter_chars()
    keep()
    sort()
#Accessor Methods

'''def filtered_anime(category, spec_categories):
    if spec_categories.len() > 0:
        anime_filter
    else:'''

valid_data()
print(len(anime))
#print(anime.to_string())
print(anime.iloc[0:50, 0])
