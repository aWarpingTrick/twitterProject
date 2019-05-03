
# Import modules
import json
import requests
from requests_oauthlib import OAuth1
import pandas as pd
from pandas.io.json import json_normalize




# OAuth credentials provided by Twitter API developer account
CONSUMER_KEY =  "YjEvGptnmmQbqzkjeOXWpnHJA"
CONSUMER_SECRET ="G7iXsL3Xk1YQpM9iWTk98r65M0L4FPPBKk1lyOWUIvdSRRYw8m"
ACCESS_TOKEN = '2194985042-Fj0cxlyuPJTfc1fgaDcKfyxyIJqsp9haue0O2XE'
ACCESS_SECRET =  "D5KZNyjAd19wzmNBlJ4eDQIHcognicPH58ynym571DyGe"

# url to pull data from for global WOEID's and Top 50 Trend Topics
# per WOEID, respectively
url1 = "https://api.twitter.com/1.1/trends/available.json"
url2 = "https://api.twitter.com/1.1/trends/place.json?id="
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# Let's define a getwoeid function which will populate a dictionary with
# CITY/WOEID key, value pairs
def getwoeids():
    mydict = dict()

    response = requests.get(url1, auth=auth)
    data = json.loads(response.text)

# Now we will iterate through the dictionary and pull out only the Canada
# WOEIDs so that we can cross reference our trends to city names after
# our next Twitter API request to trends/place
    for elem in data:
        if(elem['country'] == 'Canada'):
            mydict[elem['woeid']] = elem['name']
    return mydict

# Let's store our city/woeid pairs in a variable, mydict
mydict = getwoeids()

# This next section iterates through the dictionary items containing WOEIDs
# for Canada and uses that WOEID as a parameter for the TOP 50 lookup
for k,v in mydict.items():
    print(k,v)
    response2 = requests.get(url2 + str(k), auth=auth)
    data2 = json.loads(response2.text)
    # the data we want to access, namely, 'name' and 'tweet_number' is
    # nested within this list of dictionaries data2. Each element's first entry
    # is named 'trends' and contains a list of 50 dictionaries containing
    # 'name' and 'tweet_number' key, value pairs associated with a provided
    # WOEID
    for elem in data2:
        d = elem['trends']
        for j in range(len(d)):
            print(d[j]['name'])
            print(d[j]['tweet_volume'])
        print('\n \n \n \n')

# The dictionary entries include each top 50 trend topic and it's associated
# tweet volume within the time frame provided by Twitter API
