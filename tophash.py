import re
import json
import pandas as pd
from collections import defaultdict

#archivo = "farmers-protest-tweets-2021-03-5.json"

def toptenhash(archivo):
    mas_hash = defaultdict(lambda: 0)
    with open(archivo) as tweets:
        for tweet in tweets:
            json_tweet = json.loads(tweet)
            #Encontramos  palabras que contengan un #  re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10') [('width', '20'), ('height', '10')]
            lista = re.findall("#.*? ", json_tweet["content"])
            if lista:  #Si la lista no está vacía//hay resultados
                for hash in lista:
                    mas_hash[hash] += 1
    mas_hash = pd.json_normalize(mas_hash).transpose()
    mas_hash_ordenado= mas_hash.sort_values(by=[0], ascending=False)

    #print(mas_hash_ordenado.head(10))
    return mas_hash_ordenado.head(10)

#toptenhash(archivo)
    
  