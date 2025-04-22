import pandas as pd
import re
import ast
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
    anime = anime[anime["studios"].apply(lambda x: x.isascii())]

def drop_columns():
    anime.drop(["id", "created_at", "updated_at", "alternative_titles_en", "alternative_titles_ja", "alternative_titles_synonyms"], axis=1, inplace=True)

def remove_zero_mean():
    zero_values = anime[anime["mean"] == 0].index
    anime.drop(zero_values, inplace=True)

def remove_null():
    anime.dropna(inplace=True)

def remove_zero_popularity():
    zero_values = anime[anime["popularity"] == 0].index
    anime.drop(zero_values, inplace=True)

def sort():
    anime.sort_values(by=["popularity"], inplace=True)

def valid_data():
    remove_zero_mean()
    remove_zero_popularity()
    remove_null()
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

def mean_score(cats, spec_cats):
    #returns a 2 item list containing the mean ranking and mean rating (in that order) of the anime that fulfill the specific filters
    ani_fil = anime
    i = 0
    while i < len(cats):
        ani_fil = ani_fil[ani_fil[cats[i]] == spec_cats[i]]
        i+= 1
    mean_ranking = ani_fil['popularity'].mean()
    mean_rating = ani_fil['mean'].mean()
    return [float(mean_ranking), float(mean_rating)]

def get_specific_values(category):
    '''anime[category] = anime[category].apply(ast.literal_eval)
    column = anime[category].tolist()
    unique_values = []
    seen = set()
    for row in column:
        for value in row:
            if value not in seen:
                unique_values.append(value)
                seen.add(value)
    #print(spec_values)
    return unique_values'''
    if category == 'genres':
        return ['Action', 'Drama', 'Gore', 'Military', 'Shounen', 'Survival', 'Psychological', 'Supernatural', 'Suspense', 'Adventure', 'Fantasy', 'Comedy', 'Parody', 'Seinen', 'Super Power', 'Love Polygon', 'Romance', 'Video Game', 'School', 'Horror', 'Martial Arts', 'Historical', 'Romantic Subtext', 'Sci-Fi', 'Time Travel', 'Ecchi', 'Isekai', 'Strategy Game', 'Mecha', 'Music', 'Mythology', 'High Stakes Game', 'Mystery', 'Reincarnation', 'Sports', 'Team Sports', 'Adult Cast', 'Space', 'Award Winning', 'Avant Garde', 'Slice of Life', 'Gourmet', 'Detective', 'Vampire', 'Harem', 'Visual Arts', 'Shoujo', 'Samurai', 'Crossdressing', 'Reverse Harem', 'CGDCT', 'Delinquents', 'Gag Humor', 'Organized Crime', 'Otaku Culture', 'Workplace', 'Childcare', 'Iyashikei', 'Anthropomorphic', 'Educational', 'Medical', 'Showbiz', 'Kids', 'Mahou Shoujo', 'Combat Sports', 'Boys Love', 'Girls Love', 'Josei', 'Idols (Female)', 'Performing Arts', 'Racing']
    elif category == 'studios':
        return ['Wit Studio', 'Madhouse', 'Bones', 'A-1 Pictures', 'Pierrot', 'ufotable', 'Studio Live', 'CoMix Wave Films', 'White Fox', 'Sunrise', 'J.C.Staff', 'Kyoto Animation', 'P.A. Works', 'Toei Animation', 'MAPPA', 'asread.', 'Lerche', 'Studio Deen', 'Production I.G', 'CloverWorks', 'Studio Ghibli', 'Satelight', 'Gainax', 'Tatsunoko Production', 'Trigger', 'TMS Entertainment', 'David Production', 'Arms', 'Kinema Citrus', "Brain's Base", 'Shaft', 'TNK', '8bit', 'Manglobe', 'Tezuka Productions', 'Pierrot Plus', 'Science SARU', 'LIDENFILMS', 'Studio Bind', 'feel.', 'AIC PLUS+', 'Bridge', 'Orange', 'Doga Kobo', 'SILVER LINK.', 'Nexus', 'Graphinica', 'Nut', 'Telecom Animation Film', 'Studio VOLN', 'Seven Arcs Pictures', 'AIC Build', 'Imagin', 'Artland', 'Studio Chizu', 'Animation Do', 'Tokyo Movie Shinsha', 'GoHands', 'Gonzo', 'OLM', 'Zero-G', 'Studio Gokumi', 'Triangle Staff', 'Shuka', 'Ajia-Do', 'Production IMS', 'Zexcs', 'Connect', 'Seven Arcs', 'Pine Jam', 'Xebec', 'Passione', 'DR Movie', 'Studio 3Hz', 'Daume', 'Polygon Pictures', 'Nippon Animation', 'Shin-Ei Animation', 'Hoods Drifters Studio', 'Project No.9', 'Khara', 'TROYCA', 'Production Reed', 'Marvy Jack', 'Gallop', 'Lay-duce', 'TYO Animations', 'Signal.MD', 'ENGI', 'Silver', 'Arvo Animation', 'Studio Palette', 'Bandai Namco Pictures', 'C2C', 'SANZIGEN', 'Studio PuYUKAI', 'AIC', 'GEEK TOYS', 'Studio Colorido', 'Millepensee', 'B.CMAY PICTURES', 'EMT Squared', 'APPP', 'Seven', 'GEMBA', 'AIC Classic', 'P.I.C.S.', 'Bee Train', 'Studio Comet', 'Geno Studio', 'NAZ', 'Okuruto Noboru', 'A.C.G.T.', 'Revoroot', 'Hoods Entertainment', 'Kitty Film Mitaka Studio', 'Actas', 'Encourage Films', 'studio MOTHER', 'Studio Rikka', 'Purple Cow Studio Japan', 'HORNETS', 'Platinum Vision', 'Radix', 'Hal Film Maker', 'AIC ASTA', 'CygamesPictures', 'Maho Film', 'Asahi Production', 'AIC Spirits', "Children's Playground Entertainment", 'Studio Flad', 'Wolfsbane', 'Felix Film', 'Studio LAN', 'Haoliners Animation League', 'SynergySP', 'AXsiZ', 'production doA', 'Square Enix', 'EKACHI EPILKA', 'C-Station', 'Nomad', 'Kamikaze Douga', 'Qualia Animation']
    else:
        return list(anime[category].unique())


def pseudo_filtered(cats, spec_cats):
    #for testing purposes only
    #This is how it should work
    '''ani_fil = anime.loc[:, ['source', 'broadcast_day_of_the_week']]
    ani_fil = ani_fil[ani_fil['source'] == 'manga']
    ani_fil = ani_fil[ani_fil['broadcast_day_of_the_week'] == 'saturday']'''
    #This is the actual code
    ani_fil = anime.loc[:, cats]
    i = 0
    ani_fil = anime[anime[cats[0]] == spec_cats[0]]
    while i < len(cats):
        ani_fil = ani_fil[ani_fil[cats[i]] == spec_cats[i]]

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
# test1 = anime_occurrence(['popularity', 'broadcast_day_of_the_week'], [])
# test2 = anime_occurrence(['source', 'broadcast_day_of_the_week'], ['manga', 'saturday'])
# print(test1)
# print(len(test1))
# print(test2)
# print(len(test2))
# print(mean_score(['source', 'broadcast_day_of_the_week'], ['manga', 'saturday']))
# print(get_specific_values('broadcast_day_of_the_week'))
# print(get_specific_values('source'))
# print(get_specific_values('genres'))
# print(get_specific_values('studios'))

#print(correspondence())
