import json
import pandas as pd



#archivo = "farmers-protest-tweets-2021-03-5.json"

def toptentweets(archivo):
    seleccion = []
    with open(archivo) as tweets:
        for tweet in tweets:
            json_tweet = json.loads(tweet)
            tweet_aux = dict()
            for key in json_tweet.keys():
                    if key == "quotedTweet" and json_tweet[key] != None:
                        #Agregamos al diccionario el id del tweet retweeteado
                        tweet_aux[key] = json_tweet[key]['id']  #sobreescribirá el id del tweet retweeteado. No modifica otro atributo. 
                    if "url" not in key.lower() and json_tweet[key] != None: 
                        #hay atributos como sourcelURL, url, etc. Estos no son de interés, por lo que se descartan, al igual los que contienen NULL
                        tweet_aux[key] = json_tweet[key]
            seleccion.append(tweet_aux)
    toptweets = pd.json_normalize(seleccion)
    toptweets_ordenados = toptweets.sort_values(by=['retweetCount'], ascending=False)



    #print(toptweets_ordenados.head(10))
    return toptweets_ordenados.head(10)

#toptentweets(archivo)