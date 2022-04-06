import requests
import os
import click

from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"}

@click.command()
@click.option("--tn", prompt="Track name", help="Write track name")
def tn(tn):
    url=f"https://ru.hitmotop.com/search?q={tn}"
    r = requests.get(url, headers=headers,timeout=15)
    soup = BeautifulSoup(r.content, "html.parser")
    src = soup.find("li", class_="tracks__item track mustoggler")
    title = src.find("a", class_="track__info-l").find("div", class_="track__title").text.strip()
    link = src.find("a", class_="track__download-btn").get("href")
    artist = src.find("div", class_="track__desc").text
    download_song(link, title)
    print(f"Track name: {title} \nArtist: {artist.lower()} \nLink for download: {link}")


def download_song(link, title):
    requst_song = requests.get(link, timeout=15)
    if os.path.isfile(f"/home/jud/Music/{title}.mp3") == True: 
        return 0
    print("Скачиваю")
    with open(f"/home/jud/Music/{title}.mp3", 'wb+') as f:
        f.write(requst_song.content)


if __name__ == "__main__":
    tn()
