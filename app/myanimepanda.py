import pandas as pd
anime = pd.read_csv("static/anime.csv")

#Mutator methods
def keep_500():
    dropped_anime = anime[anime["popularity"] > 500].index
    anime.drop(dropped_anime, inplace=True)

def remove_nsfw():
    nsfw_anime = anime[anime["nsfw"] != "white"].index
    anime.drop(nsfw_anime, inplace=True)

'''def filter_chars():
#Will filter out special characters in any of the data.
    invalid_chars = anime[anime["title"].str.match("^[a-zA-Z0-9 ]")].index
    anime.drop(invalid_chars, inplace=True)'''

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

#Accessor Methods
remove_zero_mean()
remove_zero_popularity()
drop_columns()
remove_nsfw()
#filter_chars()
keep_500()
sort()
print(len(anime))
#print(anime.to_string())
print(anime.iloc[0:50, 8:12])
