# YouTube To Spotify
## Description
* Program that automates creation of playlist on Spotify from a desired youtube playlist.
* It requires the use of Spotify API as well as Google API

## How it works
1. YouTube
  * Get Playlist from YouTube and parse response to get name of artists and name of song
2. CreatePlay
  * Creates playlist in spotify.
3. SpotifySearch
  * Searches for the URI Links of the songs we got from our YouTube playlist.
  * Spotify only allows songs to be added by way of URI so this is a necessary step
4. AddSongs
  * Using our URI Links we now add songs to the playlist we created
5. YouTube-Spotify
  * Main function
  * Authorization from both APIs is done here.
  * For Spotify one needs to get the Auth Token with the scopes with the "PLAYLIST-MODIFY-PUBLIC" & "PLAYLIST-MODIFY-PRIVATE" scopes selected
  * For Google follow authorization instructions. List email address as part of the test participants to work.
  
## What you need to use
### YouTube (Google)
* Get secrets file with details of your account for authorization
* Add own account as part of users authorized to test your application
* Playlist ID
### Spotify
* Auth token for authorization
* User Id
