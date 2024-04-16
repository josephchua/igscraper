# bulk of code below is from https://www.makeuseof.com/python-instagram-fetch-data/

import instaloader
import pandas as pd
 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

debug = True # True to print Instagram account name to confirm data rows
format = "csv"

# Instagram accounts of interest to Broadway
ig_accounts = [
    "thisisvillagechurch",
    "broadwaychurch",
    "coastal_church",
    # pacific Bible College (Surrey),
    "southside_church",
# northviewcommunitychurch - Abbotsford
# theway_vancouver
# relatechurch - Surrey
# westside Church - wchurchca
# wcentralca - Worship Central Canada - Victoria
# attitude baptist church (BRA) - ibavancouver
# Columbiabiblecollege - Abbotsford
# centrechurch - Surrey
# ibavancouver (Igreja Batista Atitude Vancouver)
# gt church vancouver island (gtchurch)
# vivid.church (Vancouver & Toronto)
# Apologetics Canada
# cravechurch
# clachurch
# Surreychristianschool
# familylifecanada
# summitpc - abbotsford
# ywamvancouver
"cityreachcaresociety", # CityReach care society
# girl365
]

# if you're getting an exception when trying to load a profile below, 
# you may need to log in.  Uncomment the following ".login" line and 
# enter your account info.
# bot.login("USERNAME", "PASSWORD")

if format == "csv":
    print("Followers Count: ")

for ig_account in ig_accounts:
    # Loading a profile from an Instagram handle
    profile = instaloader.Profile.from_username(bot.context, ig_account)

    if format == "csv":
        print(profile.followers, end=' ')
        if debug:
            print(ig_account)
        else:
            print('')
    else:
        print("Username: ", profile.username)
        print("User ID: ", profile.userid)
        print("Number of Posts: ", profile.mediacount)
        print("Followers Count: ", profile.followers)
        print("Following Count: ", profile.followees)
        print("Bio: ", profile.biography)
        print("External URL: ", profile.external_url)
