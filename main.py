from urllib.parse import urlparse, parse_qs
from contextlib import suppress
from youtube_stat import YTstats

# api key
API_KEY = "AIzaSyAAXp9sXph_INz6WEa3sK2g2-nxVPuvgi8"

url="https://www.youtube.com/watch?v=SLD9xzJ4oeU&ab_channel=TopMovieClips"

def get_vid_id(url, ignore_playlist=False):
    global video_id
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com'}:
        if not ignore_playlist:
        # use case: get playlist id not current video in playlist
            with suppress(KeyError):
                return parse_qs(query.query)['list'][0]
        if query.path == '/watch':
            video_id = parse_qs(query.query)['v'][0]
            return video_id
        if query.path[:7] == '/watch/': 
            video_id = query.path.split('/')[1]
            return video_id
        if query.path[:7] == '/embed/': 
            video_id = query.path.split('/')[2]
            return video_id
        if query.path[:3] == '/v/': 
            video_id = query.path.split('/')[2]
            return video_id
   # returns None for invalid YouTube url


     

if __name__=="__main__":
    get_vid_id(url)


yt = YTstats(API_KEY,video_id)
yt.get_channel_details()






