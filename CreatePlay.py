import requests
import json

#Create playlist
def CREATE_PLAYLIST(token,user_id,name_play):
    req = requests.post(
        'https://api.spotify.com/v1/users/{}/playlists'.format(user_id),
        headers = {
            "Authorization": f"Bearer {token}"
        },
        json ={
            "name": name_play,
            "description": "Imported from YouTube",
            "public": False
        }
    )

    response = req.json()
    temp1=response['uri']
    temp2=temp1.split(':')
    final=temp2[2]
    return final


