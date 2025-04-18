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

def anime_occurrence(cats, spec_cats):
#function for bar graph/pie chart. These are graphs that would show the occurrence of anime that fulfill these categories.
#cat and spec_cat are both lists.
    if len(spec_cats) == 0:
        #returns only the specified columns
        ani_fil = anime.loc[:, cats]
        return ani_fil
    else:
        #returns only the rows with specified values in the columns listed
        ani_fil = anime.loc[:, cats]
        i = 0
        while i < len(cats):
            ani_fil = ani_fil[ani_fil[cats[i]] == spec_cats[i]]
            i+= 1
        return ani_fil

#def anime_values(cats, spec_cats):

def pseudo_filtered(cats, spec_cats):
#for testing purposes only
    #This is how it should work
    '''ani_fil = anime.loc[:, ['source', 'broadcast_day_of_the_week']]
    ani_fil = ani_fil[ani_fil['source'] == 'manga']
    ani_fil = ani_fil[ani_fil['broadcast_day_of_the_week'] == 'saturday']'''
    #This is the actual code
    ani_fil = anime.loc[:, cats]
    i = 0

    while i < len(cats):
        ani_fil = ani_fil[ani_fil[cats[i]] == spec_cats[i]]
        print(ani_fil)
        i += 1
    return ani_fil
def anime_name(popularity):
#effectively surches for anime based on index b/c ordered by popularity
    return anime.loc[anime['popularity'] == popularity]['popularity']

#Testing Area
valid_data()
print(len(anime))
#print(anime.to_string())
#print(anime.iloc[380:400, 8:12])
#print(anime_name(300))
#print(pseudo_filtered(['source', 'broadcast_day_of_the_week'], ['manga', 'saturday']))
test1 = anime_occurrence(['popularity', 'broadcast_day_of_the_week'], [])
test2 = anime_occurrence(['source', 'broadcast_day_of_the_week'], ['manga', 'saturday'])
print(test1)
print(len(test1))
print(test2)
print(len(test2))

#print(correspondence())
