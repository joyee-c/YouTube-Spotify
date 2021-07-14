import requests
import json

#add songs
def ADD_SONGS(token,play_id,u):
    req = requests.post(
        'https://api.spotify.com/v1/playlists/{}/tracks'.format(play_id),
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        },
        params = u
    )

    response=req.json()
    return response

