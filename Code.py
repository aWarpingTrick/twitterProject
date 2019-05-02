
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

# Instead of asking the user for a country entry, I've inserted the value here.
country = 'Canada'

# load json response from "GET trends/available" into dataframe representing WOEID's belonging
# to twitter topics
r = requests.get(url1, auth=auth)
raw = json.loads(r.content)
df1 = pd.DataFrame.from_dict(raw, orient='columns')
list = []

# Iterates through df1 rows and pulls the WOEID labels for all rows with
# country column values == 'Canada' (or the country selected)
for i in range(len(df1)):
    if df1['country'][i] == country:
        list.append(df1['woeid'][i])
# Prints out a reflection of the WOEID's being used in the trend topic lookup
# which follows
print("The woeid's associated with " + country + " are:")
print(list)

# Initialize two empty dataframes.  The first will hold the original json
# response loaded into a row entry within df2 for every WOEID at the time
# the API data was requested

# The second will hold the further processed JSON row entries from df2.
# More specifically, we need to un-nest certain row entries to access fully
df2 = pd.DataFrame([])
df3 = pd.DataFrame([])

# Loops through the populated WOEID list for 'Canada' and requests in addition
# to the url2 address as you can see below.

# df2 starts off empty and gets appended with request nested JSON response2
# this dataframe, after iterated through, holds the top 50 twitter trend Topics
# from the time of the request, for all WOEID's searched

# df3 takes the initial empty value as well, and through the for loop will adopt
# and expand into separate columns, each dictionary entry for every WOEID from
# df2.

# The dictionary entries include each top 50 trend topic and it's associated
# tweet volume within the time frame provided by Twitter API
for i in list:
    response2 = requests.get(url2 + str(i), auth=auth)
    data2 = json.loads(response2.text)
    result = json_normalize(data2)
    df2 = df2.append(pd.DataFrame.from_dict(result, orient='columns'))
    df3 = df3.append(df2['trends'].apply(pd.Series))

# When we are finished with the script, we want to export our dataframe to a
# csv that will be furter updated daily by running this script
# and an associated batch file on Window's Task Scheduler
export_csv = df3.to_csv('my_csv.csv', mode = 'a', header=False, index=False)

# Batch file, Run_script.bat, was created simply in the format of
# "C:\Path_to_folder\python.exe" "C:\Path_to_folder\twitterproject\code.py"
