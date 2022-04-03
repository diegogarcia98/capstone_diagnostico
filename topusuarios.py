import json
import pandas as pd
from collections import defaultdict


#archivo = "farmers-protest-tweets-2021-03-5.json"

def toptenusuarios(archivo):
    usuarios = defaultdict(int)
    with open(archivo) as tweets:
        for tweet in tweets:
            json_tweet = json.loads(tweet)
            usuarios[json_tweet["user"]["username"]] +=1

    
    topusuarios = pd.json_normalize(usuarios).transpose()
    topusuarios_ordenados = topusuarios.sort_values(by=[0], ascending=False)
    #print(topusuarios_ordenados.head(10))
    return topusuarios_ordenados.head(10)

#toptenusuarios(archivo)