import json

credentials = {}
credentials['CONSUMER_KEY'] =  "YjEvGptnmmQbqzkjeOXWpnHJA"
credentials['CONSUMER_SECRET'] ="G7iXsL3Xk1YQpM9iWTk98r65M0L4FPPBKk1lyOWUIvdSRRYw8m"
credentials['ACCESS_TOKEN'] = '2194985042-Fj0cxlyuPJTfc1fgaDcKfyxyIJqsp9haue0O2XE'
credentials['ACCESS_SECRET'] =  "D5KZNyjAd19wzmNBlJ4eDQIHcognicPH58ynym571DyGe"

with open("twitter_credentials.json", "w") as file:
    json.dump(credentials,file)
