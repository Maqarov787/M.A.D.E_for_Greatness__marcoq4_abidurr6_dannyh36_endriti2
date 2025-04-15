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
#Warning: Consulted with the AI overlords (GPT-4o) to construct this method. The prompt given was "how would I filter out rows of data in python pandas that contain non-ascii characters?
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

def correspondence():
#function for line graph
    pop = anime['popularity'].tolist()
    mean = anime['mean'].tolist()
    return [pop, mean]

def filtered_anime(cats, spec_cats):
#function for bar graph/pie chart
#cat and spec_cat are both arrays. cat has to have at least one
    if len(spec_cats) == 0:
        ani_fil = anime.loc[:, cats]
        return ani_fil
    else:
        ani_fil = anime[cats]
        return "Test. cats not working probably"

def anime_name(popularity):
    return anime.loc[anime['popularity'] == popularity]

#Testing Area
valid_data()
print(len(anime))
#print(anime.to_string())
#print(anime.iloc[380:400, 8:12])
#print(anime_name(300))
test1 = filtered_anime(['popularity', 'genres'], [])
print(test1)
print(len(test1))

#print(correspondence())
