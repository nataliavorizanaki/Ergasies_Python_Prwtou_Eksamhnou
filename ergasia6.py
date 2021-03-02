#This is the authorization option bearer token I used:
#AAAAAAAAAAAAAAAAAAAAAJTlLAEAAAAAJiJQD415WqiPVT2%2FcAOnEonTBsg%3D3tFfEjVHKYxNc1rnOKN8oAWqHB9fmtnancU0jkVeu5KwZuw848
import tweepy
import sys
import requests
import os
import json
# -*- coding: utf-8 -*-

def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url(userId):
#    query = "from:twitterdev -is:retweet"
#    query = "from:arianagrande -is:retweet"
    query = "max_results=10"
#    query= "-is:retweet"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
#    tweet_fields = "tweet.fields=author_id"
    tweet_fields = "tweet.fields=author_id,conversation_id,created_at"
#    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
#        query, tweet_fields)
    url = "https://api.twitter.com/2/users/{}/tweets?{}&{}".format(userId,
        tweet_fields, query)

    #print(url)

    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_user_id(username, headers):
    url_userid = "https://api.twitter.com/2/users/by/username/" + username
    response = requests.request("GET", url_userid, headers=headers)
    #print(response.status_code)
    json_user = response.json()
    data_dict = json_user["data"]
    user_id = data_dict["id"]
    #print(user_id)
    return user_id

def main():
    flag = True
    while flag == True:
        try:
           username=input("Insert your username:  ")
           username=str(username)
           username1 = username.replace("_","")
           if (username1.isalnum()==True and username1.isdecimal() == False and len(username1) <= 15):
                flag = False
           else:
                if len(username1) > 15:
                    print("The maximum length of the username is 15 characters.")
                else:
                    print("The length of the username is okay but try another username please.")
                continue

        except:
            print("Error")
            continue





    bearer_token = auth()
#    print(bearer_token)
    headers = create_headers(bearer_token)
    userId = get_user_id(username, headers)
    url = create_url(userId)
    json_response = connect_to_endpoint(url, headers)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    t = list(json_response.keys())
    #print("The keys are:",t)
# In this table, the actual Tweets's texts are stored
    for x in range(10):
       t1=json_response["data"]
       t2=t1[x]
       t3=t2["text"]
       #print(t3)
       t4=t3.split(" ")
       #print(t4)
       if x==0:
           tweets=t4
           continue
       else:
           tweets.extend(t4)
    #print("\n"*4)
    #print("All tweets splitted to words:", tweets)
    #print("\n"*4)
    tweets1=sorted(tweets, key=len, reverse=False)
    #print(tweets1)
    print("\n"*4)
    print("The five shortest words are:")
    for i in range(5):
        print(tweets1[i])
    tweets2=sorted(tweets, key=len, reverse=True)
    #print(tweets2)
    print("\n"*4)
    print("The five longest words are:")
    for i in range(5):
        print(tweets2[i])






if __name__ == "__main__":
    main()
