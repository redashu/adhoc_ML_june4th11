#!/usr/bin/python3

import tweepy
from  textblob import TextBlob
#  defining consumer key and secret  
#  making connection with twitter api 
c_key=""

c_sec=""

#  token key and secret
#  to search and get information u need to use token 
t_key=""

t_sec=""

#  connting twitter APi 
auth_session=tweepy.OAuthHandler(c_key,c_sec)

#print(dir(auth_session))

# setting  , sending  token key and secret
auth_session.set_access_token(t_key,t_sec)

#  now accessing  API  

api_connect=tweepy.API(auth_session)

#  searching  data  
topic=api_connect.search('Trumph')

for  i  in  topic:
    #  tokenized and clean   
    blob_data=TextBlob(i.text)
    # applying sentiment  output will be polarity 
    print(blob_data.sentiment)

















