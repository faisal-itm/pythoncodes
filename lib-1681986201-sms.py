import tweepy
import json
import time
import datetime


# Authentication details. Enter your own twitter app keys here.
consumer_key = "vYvazxSr4gz19j2UNjQw8W6Fz"
consumer_secret = "QrEoXHQvz7bxKVrniSpEvC89GLDNk0Kua15LpIBYAVhTOtq6Qz"
access_key = "1557317528-L7MMHuKOnC73wbCBLpY9G6JwwounVSHn25aTDRB"
access_secret = "img3XUX9tShwOxBTunHs7wWmvisiTnK0QmUFnOyLHfODc"


# Enter the hashtag you want to search for here.
accountvar = "Pakistan"
# getting the current date and time.
t = datetime.datetime.now()
# sorting the acquired date and time into the format we want as Windows   # doesn't allow us to include : in file names.
a = t.strftime('%Y-%m-%d-%H-%M')
# specifying the output file name.
outputfilejson =  accountvar+"_"+str(a)+".json"
# This is the listener, resposible for receiving data.


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search_tweets,
              q=accountvar,
              count=10,
              lang="en",
              tweet_mode='extended').items(100)


tweets_list = []
for tweet in tweets:
    tweets_list.append({
        "id"         : tweet.id,
        "id_str"         : tweet.id_str,
        "text" : tweet.full_text,
        "source" : tweet.source,
        "truncated": tweet.truncated,
        "user_tw":
        {
                   "id":tweet.user.id,
                   "id_str":tweet.user.id_str,
                   "name":tweet.user.name,
                   "screen_name":tweet.user.screen_name,
                   "location":tweet.user.location,
                   "url":tweet.user.url,
                   "description":tweet.user.description,
                   "translator_type":tweet.user.translator_type,
                   "protected":tweet.user.protected,
                   "verified":tweet.user.verified,
                    "followers_count":tweet.user.followers_count,
                   "friends_count":tweet.user.friends_count,
                   "listed_count":tweet.user.listed_count,
                   "favourites_count":tweet.user.favourites_count,
                   "created_at":str(tweet.user.created_at),
                   "utc_offset":tweet.user.utc_offset,
                    "time_zone":tweet.user.time_zone
        }

    })

with open(outputfilejson, 'w') as fout:
    json.dump(tweets_list, fout)