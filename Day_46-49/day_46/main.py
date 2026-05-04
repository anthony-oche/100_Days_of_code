from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri= "https://example.com",
    client_id="dd98b18f15ca4b3ab1612a7398e2b2ba",
    client_secret="cdd3d8ee550a4576bf16a05bca5cac6c",
    show_dialog=True,
    cache_path="token.txt",
    username="Switch",

))


date = input("What year you would like to travel to? Type the date in this format YYY-MM-DD : ")
year = date.split("-")[0]
print(year)

response = requests.get(url=f"https://www.officialcharts.com/charts/singles-chart/{date}/7501/")
chart_html = response.text

soup = BeautifulSoup(chart_html, "html.parser")

music_chart = soup.select(selector=".chart-artist span")
song_list = []

for artist in music_chart:
    top = artist.getText()
    song_list.append(top)


for artist in song_list:
    results = sp.search(q=f"{artist}:{year}", type="track", limit= 5)
    print(results)

    for track in results["tracks"]["items"]:
        print("song:", "-", track["name"])
        print("Release Date:", track["album"]["release_date"])
        print("-"*40)



