import requests


# get the current news from the database

base_url = "http://api.steampowered.com"

def get_cs2_news():
    url = f"{base_url}/ISteamNews/GetNewsForApp/v0002/?appid=730&count=4&maxlength=300&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to get data {response.status_code}")


cs2_info = get_cs2_news()

if cs2_info:
    #seperate the news items into there own veriables
    appnews = cs2_info["appnews"]
    newsitems = appnews["newsitems"]
    latestupdate = newsitems[0]
    update2 = newsitems[1]
    update3 = newsitems[2]
    update4 = newsitems[3]

    #finds the titles in the json file
    latestupdatetitle = latestupdate["title"]
    update2title = update2["title"]
    update3title = update3["title"]
    update4title = update4["title"]
    #find urls in the json file
    latestupdateurl = latestupdate["url"]
    update2url = update2["url"]
    update3url = update3["url"]
    update4url = update4["url"]
    #find the contents of the news items
    latestupdatecontent = latestupdate["contents"]
    update2content = update2["contents"]
    update3content = update3["contents"]
    update4content = update4["contents"]