
#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import json
import requests
from requests_oauthlib import OAuth1
import pandas as pd
from pandas.io.json import json_normalize


# OAuth credentials provided by API developer
CONSUMER_KEY =  "YjEvGptnmmQbqzkjeOXWpnHJA"
CONSUMER_SECRET ="G7iXsL3Xk1YQpM9iWTk98r65M0L4FPPBKk1lyOWUIvdSRRYw8m"
ACCESS_TOKEN = '2194985042-Fj0cxlyuPJTfc1fgaDcKfyxyIJqsp9haue0O2XE'
ACCESS_SECRET =  "D5KZNyjAd19wzmNBlJ4eDQIHcognicPH58ynym571DyGe"

# url to pull data from
url1 = "https://api.twitter.com/1.1/trends/available.json"
url2 = "https://api.twitter.com/1.1/trends/place.json?id="
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

country = 'Canada'

# load json response from "GET trends/available" into dataframe representing WOEID's belonging
# to twitter topics
response = requests.get(url1, auth=auth)
data= json.loads(response.text)
df1 = pd.DataFrame.from_dict(data, orient='columns')

list = []
for i in range(len(df1)):
    if df1['country'][i] == country:
        list.append(df1['woeid'][i])

print("The woeid's associated with " + country + " are:")
print(list)
list_df = []
df2 = pd.DataFrame([])
for i in list:
    response2 = requests.get(url2 + str(i), auth=auth)
    data2 = json.loads(response2.text)
    result = json_normalize(data2)
    df2 = df2.append(pd.DataFrame.from_dict(result, orient='columns'))
df2.to_csv('my_csv.csv', mode = 'a', header=False, index=False)
