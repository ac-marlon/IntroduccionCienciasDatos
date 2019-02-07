import tweepy
import numpy as np
import statistics as st
import pandas as pd 

"""
Candidatos para la alcaldia de Bogota DC en el 2019:

(A) Hollman Morris (Movimiento Alternativo Indigena)
(B) Diego Molano | (C) Angela Garzon | (D) Samuel Hoyos (Centro Democratico)
(E) Antonio Navarro Wolf | (F) Claudia Lopez (Polo Democratico)
(G) Jorge Rojas (Colombia Humana)
(H) Miguel Uribe Turbay (Partido Liberal)
(I) Carlos Fernando Galan (Nuevo Liberalismo)
"""

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

seguidores_A = api.get_user('hollmanmorris').followers_count
seguidores_E = api.get_user('navarrowolff').followers_count
seguidores_F = api.get_user('claudialopez').followers_count

tweets_A = api.user_timeline('hollmanmorris')
tweets_E = api.user_timeline('navarrowolff')
tweets_F = api.user_timeline('claudialopez')

datos_A = pd.DataFrame(data = [tweet.text for tweet in tweets_A], columns = ['Tweets'])
datos_E = pd.DataFrame(data = [tweet.text for tweet in tweets_E], columns = ['Tweets'])
datos_F = pd.DataFrame(data = [tweet.text for tweet in tweets_F], columns = ['Tweets'])

datos_A['Longitud'] = np.array([len(tweet.text) for tweet in tweets_A])
datos_A['Likes'] = np.array([tweet.favorite_count for tweet in tweets_A])
datos_A['ReTweets'] = np.array([tweet.retweet_count for tweet in tweets_A])

datos_E['Longitud'] = np.array([len(tweet.text) for tweet in tweets_E])
datos_E['Likes'] = np.array([tweet.favorite_count for tweet in tweets_E])
datos_E['ReTweets'] = np.array([tweet.retweet_count for tweet in tweets_F])

datos_F['Longitud'] = np.array([len(tweet.text) for tweet in tweets_F])
datos_F['Likes'] = np.array([tweet.favorite_count for tweet in tweets_F])
datos_F['ReTweets'] = np.array([tweet.retweet_count for tweet in tweets_F])

def tend_central_y_disp_tweets(candidato, longitud, likes, rt, histTweets):
	mediaLong = st.mean(longitud)
	mediaLikes = st.mean(likes)
	mediaRT = st.mean(rt)

	print("\t DATOS DEL CANDIDATO: " + candidato)
	print("Longitud media de Tweets: " + str(mediaLong))
	print("Cantidad de likes en promedio: " + str(mediaLikes))
	print("Cantidad de ReTweets en promedio: " + str(mediaRT) + "\n")

	medianaLong = st.median(longitud)
	medianaLikes = st.median(likes)
	medianaRT = st.median(rt)

	print("Tweet de longitud mediana: " + str(medianaLong))
	print("Mediana de likes: " + str(medianaLikes))
	print("Mediana de ReTweets: " + str(medianaRT) + "\n")

	tweetMasLikes = np.max(likes)
	tweetMasRT = np.max(rt)
	mejorTweetLikes = histTweets[histTweets.Likes == tweetMasLikes].index[0]
	mejorTweetRT = histTweets[histTweets.ReTweets == tweetMasRT].index[0]

	print("El tweet con mas <Me Gusta> es: \n" + str(histTweets['Tweets'][mejorTweetLikes]))
	print("Numero de <Me Gusta>: " + str(tweetMasLikes))
	print("Con una longitud de (caracteres): " + str(histTweets['Longitud'][mejorTweetLikes]) + "\n")

	print("El tweet con mas <RT> es: \n" + str(histTweets['Tweets'][mejorTweetRT]))
	print("Numero de <Me Gusta>: " + str(tweetMasRT))
	print("Con una longitud de (caracteres): " + str(histTweets['Longitud'][mejorTweetRT]) + "\n")

	rangoLong = max(longitud) - min(longitud)
	rangoLikes = max(likes) - min(likes)
	rangoRT = max(rt) - min(rt)

	varLong = st.pvariance(longitud)
	varLikes = st.pvariance(likes)
	varRT = st.pvariance(rt)

	desvEstandLong = np.std(longitud)
	desvEstandLikes = np.std(likes)
	desvEstandRT = np.std(rt)

	print("Rango, varianza y desviacion estandar de la longitud de los tweets: ")
	print(str(rangoLong) + " | " + str(varLong) + " | " + str(desvEstandLong))
	print("Rango, varianza y desviacion estandar del numero de likes: ")
	print(str(rangoLikes) + " | " + str(varLikes) + " | " + str(desvEstandLikes))
	print("Rango, varianza y desviacion estandar de la cantidad de retweets: ")
	print(str(rangoRT) + " | " + str(varRT) + " | " + str(desvEstandRT) + "\n")

	correLongLikes = np.corrcoef(longitud, likes)
	correLongRT = np.corrcoef(longitud, rt)
	correLikesRT = np.corrcoef(likes, rt)

	print("La correlacion entre longitud y likes es: " + str(correLongLikes[0][1]))
	print("La correlacion entre longitud y retweets es: " + str(correLongRT[0][1]))
	print("La correlacion entre likes y retweets es: " + str(correLikesRT[0][1]))

	print("---------------------------------------------\n\n")

tend_central_y_disp_tweets("hollmanmorris", datos_A['Longitud'], datos_A['Likes'], datos_A['ReTweets'], datos_A)
tend_central_y_disp_tweets("navarrowolff", datos_E['Longitud'], datos_E['Likes'], datos_E['ReTweets'], datos_E)
tend_central_y_disp_tweets("claudialopez", datos_F['Longitud'], datos_F['Likes'], datos_F['ReTweets'], datos_F)
