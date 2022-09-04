
from turtle import title
from xml.dom.minidom import Document
from urllib.request import urlopen
import json

class YTstats:
    def __init__(self, api_key, video_id):
        self.api_key = api_key
        self.video_id = video_id
        self.channel_statistics = None
        self.channel_snippet = None
        self.channel_contentDetails = None
    def get_channel_details(self):
        url = f'https://youtube.googleapis.com/youtube/v3/videos?key={self.api_key}&part=snippet&part=statistics&part=contentDetails&id={self.video_id}'

        print(url)

        # store the response of URL
        response = urlopen(url)
        
        # storing the JSON response 
        # from url in data
        data_json = json.loads(response.read())
        
        # print the json response

        # print(data_json)

        # title,like,viewcount,duration,description
        title=data_json['items'][0]['snippet']['title']
        description = data_json['items'][0]['snippet']['description']
        viewcount = data_json['items'][0]["statistics"]["viewCount"]
        duration = data_json['items'][0]["contentDetails"]["duration"].removeprefix('PT')
        likecount = data_json['items'][0]['statistics']["likeCount"]
        print('title is',title)
        print('description is',description )
        print('viewcount is',viewcount)
        print('duration is',duration)
        print('likecount is',likecount)

        # print()
        

        




       
