import json
import re
import requests
import html

class Helper:
    def __init__(self):
        pass

    def id_from_url(self, url: str):
        return url.rsplit("/", 1)[1]

class YouTubeStats:
    def __init__(self, url: str):
        #self.json_url = urllib.request.urlopen(url)
        self.json_url = requests.get(url)
        self.data = json.loads(self.json_url.text)
        
    def print_data(self):
        print(self.data)

    def get_video_title(self):
        return self.data["items"][0]["snippet"]["title"]

def sam(Kara):
    # customizable opening words
    opening = 'Sam'

    api_key = "AIzaSyC1t1JwqEFSe4sd3fa7OmgKfLMKd2zzFeA"

    link_file = "links.csv"

    with open(link_file, "r") as f:
        content = f.readlines()

    content = list(map(lambda s: s.strip(), content))
    content = list(map(lambda s: s.strip(','), content))

    helper = Helper()

    for youtube_url in content:
        video_id = helper.id_from_url(youtube_url)
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={video_id}&maxResults=1&order=date&type=video&key={api_key}"
        yt_stats = YouTubeStats(url)
        title = html.unescape(yt_stats.get_video_title())
    
    with open('temp.txt', 'r') as f:
        temp = f.read()

    if title = tmp:
        yes = "did not"
        name = ""
    else :
        yes = "did"
        f = open("tmp.txt", "w")
        f.write(title)
        f.close
        name = "called {title}"

    line = '{} {} upload  a video {}.'.format(opening, yes, name)
    Kara.speak(line)