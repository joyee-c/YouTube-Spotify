import requests
import json

#search for a track
def SEARCH_TRACK(token,p,art):
    req = requests.get(
        'https://api.spotify.com/v1/search',
        headers = {
            "Authorization": f"Bearer {token}"
        },
        params=p
    )

    response = req.json()
    #print(req.text)

    allPossible = response['tracks']['items']
    #print(allPossible.text)
    uri_link=''

    for allA in allPossible:
        name_artist=[findA['name'] for findA in allA['artists'] ]
        if art in name_artist:
            link=allA['uri'].split(':')
            uri_link=link[2]
            break
    return uri_link




