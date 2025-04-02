import pandas as pd
anime = pd.read_csv("static/anime.csv")

def anime_info():
    anime.info(verbose = False)

def keep_1000():
    for x in anime.index:
        if anime.loc[x, "popularity"] > 1000:
            anime.drop(anime.loc[anime["popularity"]==anime.loc[x, "popularity"]].index, inplace=True)

keep_1000()
anime_info()
