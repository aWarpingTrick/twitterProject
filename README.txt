1. Import json, requests, OAuth1, and sqlite3 modules.

2. Authenticate Twitter API Developer access.

3. We are working with two urls from Twitter's API.

url1 = "https://api.twitter.com/1.1/trends/available.json"

url2 = "https://api.twitter.com/1.1/trends/place.json?id="

4. Connect ourselves to db1 SQL database and create a table with columns
for country, WOEID, date, city, tweet_topic, and tweet_volume.

5. Define a function to retrieve WOEIDs from url1 associated with trend topics in Canada and store 
in a dictionary.

6. Iterate through dictionary and use WOEIDs as inputs into second JSON request to url2 to
retrieve trend topic data and insert these values into our SQL database rows.

7. Commite changes to our database and close.

8. Repeat this script automatically from Windows Task Scheduler daily with a batch file.