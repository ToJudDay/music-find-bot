import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"}


def get_data(url):
    itertion_count = 0
    r = requests.get(url)
    with open("index.html", "w") as file:
        file.write(r.text)
    soup = BeautifulSoup(r.text, "lxml")
    src = soup.find_all("li", class_="tracks__item track mustoggler")
    for content in src:
        if itertion_count == 1:
            print("5 tracks shown")
            break
        title = content.find(
            "a", class_="track__info-l").find("div", class_="track__title").text.strip()
        # print(title)
        artist = content.find("div", class_="track__desc").text
        link = content.find("a", class_="track__download-btn").get("href")
        print(
            f"Track name: {title} \nArtist: {artist} \nLink for download: {link}\n ")
        itertion_count += 1
        download_song(link, title, artist)
        # wget.download(link)


def download_song(link, title, artist):
    # full_link = f"https://musify.club{link}"
    requst_song = requests.get(link, timeout=10)
    # track_save = open(f"{title} - {artist}.mp3", "wb")
    # # track_save.write(requst_song.content)
    # with open(f"{title} - {artist}.mp3", 'wb') as file:
    #     for chunk in requst_song.iter_content(chunk_size=1024 * 1024):
    #         if chunk:
    #             file.write(chunk)
    with open(f"tracks/{title} - {artist}.mp3", 'wb') as f:
        f.write(requst_song.content)


def main():
    track = input("Write track name: ")
    get_data(url=f"https://ru.hitmotop.com/search?q={track}")


if __name__ == "__main__":
    main()
