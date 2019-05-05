<<<<<<< HEAD

# Import modules
import json
import requests
from requests_oauthlib import OAuth1
import sqlite3



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

# load json response from "GET trends/available" into dataframe representing WOEID's belonging
# to twitter topics



# Initiate sqlite3 objects to use
sqlite_file = 'C:/Users/warin/Desktop/APIs/Git Hub/Twitterproject/my_db.sqlite'
table_name = 'Twitter_Top_50_Trending_Topics_Across_Canada'
column_1 = 'City'
column_11 = 'Woeid'
column_111 = 'Date'
column_2 = 'Name'
column_3 = 'Tweet_Volume'
column_typeT = 'TEXT'
column_typeI = 'INTEGER'


con = sqlite3.connect('C:/Users/warin/Desktop/APIs/Git Hub/twitterProject/my_db1.db')
print("Opened database successfully")

# Connecting to the database file
c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS table_name2 (column_1111 VARCRCHAR(100), column_11 KEY, column_111 VARCRCHAR(100), column_1 VARCRCHAR(100), column_2 VARCRCHAR(100), column_3 INTEGER DEFAULT 0);''')
# Create a new SQLite table with 1 column
# c.execute("ALTER TABLE {tn} ADD COLUMN '{cn1}' {ct}".format(tn=table_name,
#     cn1 = column_1, ct= column_typeT))
# c.execute("ALTER TABLE {tn} ADD COLUMN '{cn2}' {ct}".format(tn=table_name,
#     cn2 = column_2, ct= column_typeT))
# c.execute("ALTER TABLE {tn} ADD COLUMN '{cn3}' {ct}".format(tn=table_name,
#     cn3 = column_3, ct= column_typeI))

def getwoeids():
    mydict = dict()

    response = requests.get(url1, auth=auth)
    data = json.loads(response.text)


    for elem in data:
        if(elem['country'] == 'Canada'):
            mydict[elem['woeid']] = elem['name']
    return mydict
mydict = getwoeids()

for k,v in mydict.items():
    print(k,v)
    response2 = requests.get(url2 + str(k), auth=auth)
    data2 = json.loads(response2.text)
    # the data we want to access, namely, 'name' and 'tweet_number' is
    # nested within this list of dictionaries data2. Each element's first entry
    # is named 'trends' and contains a list of 50 dictionaries containing
    # 'name' and 'tweet_number' key, value pairs associated with a provided
    # WOEID
    # c.execute('''INSERT INTO table_name (column_1) VALUES (?)''', (v,))
    for elem in data2:
        d = elem['trends']
        for j in range(len(d)):
            a = d[j]['name']
            print(a)
            b = d[j]['tweet_volume']
            print(b)
            date = elem['as_of']
            country = 'Canada'
            c.execute('''INSERT INTO table_name2 (column_1111, column_11, column_111, column_1, column_2, column_3) VALUES (?, ?, ?, ?, ?, ?)''', (country, k, date, v, a, b))
        print('\n \n \n')
con.commit()
con.close()
# The dictionary entries include each top 50 trend topic and it's associated
# tweet volume within the time frame provided by Twitter API



# When we are finished with the script, we want to export our dataframe to a
# csv that will be furter updated daily by running this script
# # and an associated batch file on Window's Task Scheduler
# export_csv = df3.to_csv('my_csv.csv', mode = 'a', header=False, index=False)

# Batch file, Run_script.bat, was created simply in the format of
# "C:\Path_to_folder\python.exe" "C:\Path_to_folder\twitterproject\code.py"
||||||| merged common ancestors
=======

# Import modules
import json
import requests
from requests_oauthlib import OAuth1
import pandas as pd
from pandas.io.json import json_normalize
import sqlite3
from sqlite3 import Error
import os.path



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

# load json response from "GET trends/available" into dataframe representing WOEID's belonging
# to twitter topics



# Initiate sqlite3 objects to use
sqlite_file = 'C:/Users/warin/Desktop/APIs/Git Hub/Twitterproject/my_db.sqlite'
table_name = 'Twitter_Top_50_Trending_Topics_Across_Canada'
column_1 = 'City'
column_11 = 'Woeid'
column_2 = 'Name'
column_3 = 'Tweet_Volume'
column_typeT = 'TEXT'
column_typeI = 'INTEGER'


con = sqlite3.connect('C:/Users/warin/Desktop/APIs/Git Hub/twitterProject/my_db4.db')
print("Opened database successfully")

# Connecting to the database file
c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS table_name (column_11 KEY, column_1 VARCRCHAR(100), column_2 VARCRCHAR(100), column_3 INTEGER DEFAULT 0);''')
# Create a new SQLite table with 1 column
# c.execute("ALTER TABLE {tn} ADD COLUMN '{cn1}' {ct}".format(tn=table_name,
#     cn1 = column_1, ct= column_typeT))
# c.execute("ALTER TABLE {tn} ADD COLUMN '{cn2}' {ct}".format(tn=table_name,
#     cn2 = column_2, ct= column_typeT))
# c.execute("ALTER TABLE {tn} ADD COLUMN '{cn3}' {ct}".format(tn=table_name,
#     cn3 = column_3, ct= column_typeI))

def getwoeids():
    mydict = dict()

    response = requests.get(url1, auth=auth)
    data = json.loads(response.text)


    for elem in data:
        if(elem['country'] == 'Canada'):
            mydict[elem['woeid']] = elem['name']
    return mydict
mydict = getwoeids()

for k,v in mydict.items():
    print(k,v)
    response2 = requests.get(url2 + str(k), auth=auth)
    data2 = json.loads(response2.text)
    # the data we want to access, namely, 'name' and 'tweet_number' is
    # nested within this list of dictionaries data2. Each element's first entry
    # is named 'trends' and contains a list of 50 dictionaries containing
    # 'name' and 'tweet_number' key, value pairs associated with a provided
    # WOEID
    # c.execute('''INSERT INTO table_name (column_1) VALUES (?)''', (v,))
    for elem in data2:
        d = elem['trends']
        for j in range(len(d)):
            a = d[j]['name']
            print(a)
            b = d[j]['tweet_volume']
            print(b)
            c.execute('''INSERT INTO table_name (column_11, column_1, column_2, column_3) VALUES (?, ?, ?, ?)''', (k, v, a, b))
        print('\n \n \n')
con.commit()
con.close()
# The dictionary entries include each top 50 trend topic and it's associated
# tweet volume within the time frame provided by Twitter API



# When we are finished with the script, we want to export our dataframe to a
# csv that will be furter updated daily by running this script
# # and an associated batch file on Window's Task Scheduler
# export_csv = df3.to_csv('my_csv.csv', mode = 'a', header=False, index=False)

# Batch file, Run_script.bat, was created simply in the format of
# "C:\Path_to_folder\python.exe" "C:\Path_to_folder\twitterproject\code.py"
>>>>>>> 67d0c5979e703e65c3040e5ae2eac306de64e37c
