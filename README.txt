# Install packages:
pandas
sqlite3 (did not implement, will in next version)
requests
json


# Import modules


# OAuth credentials provided by Twitter API developer account


# url to pull data from for global WOEID's and Top 50 Trend Topics
# per WOEID, respectively


# Instead of asking the user for a country entry, I've inserted the value here.
country = 'Canada'

# load json response from "GET trends/available" into dataframe representing WOEID's belonging
# to twitter topics


# Iterates through df1 rows and pulls the WOEID labels for all rows with
# country column values == 'Canada' (or the country selected)

# Prints out a reflection of the WOEID's being used in the trend topic lookup
# which follows


# Initialize two empty dataframes.  The first will hold the original json
# response loaded into a row entry within df2 for every WOEID at the time
# the API data was requested

# The second will hold the further processed JSON row entries from df2.
# More specifically, we need to un-nest certain row entries to access fully


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


# When we are finished with the script, we want to export our dataframe to a
# csv that will be furter updated daily by running this script
# and an associated batch file on Window's Task Scheduler


# Batch file, Run_script.bat, was created simply in the format of
# "C:\Path_to_folder\python.exe" "C:\Path_to_folder\twitterproject\code.py"