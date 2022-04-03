#importamos librearías útiles
import json #Para leer JSON
import pandas as pd
from collections import defaultdict
import datetime

#archivo = "farmers-protest-tweets-2021-03-5.json"

def toptendias(archivo):
    contador_dias = defaultdict(int)
    # formato de dias "2021-03-30T03:33:46+00:00"
    with open(archivo) as tweets:
        for tweet in tweets:
            json_tweet = json.loads(tweet)
            fecha = datetime.datetime.strptime(json_tweet["date"].split("T")[0], "%Y-%m-%d").date() 
            # la fecha queda de esta forma 2021-03-30
            contador_dias[fecha] += 1 
    top_dias = pd.json_normalize(contador_dias).transpose()
    top_dias_ordenado = top_dias.sort_values(by=[0], ascending=False)
    #print(top_dias_ordenado.head(10))
    return top_dias_ordenado.head(10)


#toptendias(archivo)