from YouTube import GET_PLAY
from AddSong import ADD_SONGS
from CreatePlay import CREATE_PLAYLIST
from SpotifySearch import SEARCH_TRACK

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json
import requests

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
user_id ='vxplq4vazhlzlx9a617fxyfa7'
AUTH_TOKEN = 'BQDyzX_2sue8LrG62Z5PN81jq411QnpbsnEan_1uZ7yagZ_CJ2NZv8UB6azoei1DKrRnVzLEw2pS_UFb5zY0uqAvPZomIgNppRrkj4o1ZXRJ7zrCpXow6h-iqjhw_vGZJUB65p5hnb5MdUL5nR26_SzvIpYBEDpHAiAdg8Rp0k7RMTI5jFH_nLJZVbYs54pWpCjwVieeXeRhOqJjVxrtslIkCTFQcBcKxwQb_Cls2_o'

def main():
# Get playlist and songs from youtube
    song_artist = GET_PLAY()
    artist_track={}
    for item in song_artist:
       first=item.split('-')
       tempArtist = first[0].split(",")
       finalArtsist=tempArtist[0].strip()
       tempSong=first[1].split("(")
       finalSong=tempSong[0].strip()
       if finalArtsist in artist_track:
           artist_track[finalArtsist].append(finalSong)
       else:
           artist_track[finalArtsist]=[finalSong]
    print(artist_track)
# Create new Playlist
    New_playlist = CREATE_PLAYLIST(AUTH_TOKEN,user_id)
# GET URI LINKS
    uri_list=[]

    for artist, song in artist_track.items():
        for x in artist_track[artist]:
            info_track = {
            'q': x,
            'type': 'track'
            }
            uri_list.append(SEARCH_TRACK(AUTH_TOKEN,info_track,artist))

# ADD SONGS
    for link in uri_list:
        if len(link)==0:
            pass
        else:
            uri_={
                'uris' : 'spotify:track:'+link,
                }
            success = ADD_SONGS(AUTH_TOKEN,New_playlist,uri_)
        print(success)
#main
if __name__ == "__main__":
    main()


     