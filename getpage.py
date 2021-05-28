import requests
import json

from requests.api import request

headers = { 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'}
cookies = {'sessionid':'2113549053%3AjRELxFuxiS2pO5%3A15'}

def get_info_page(user):  

    response = requests.get('https://www.instagram.com/'+user+'/?__a=1',headers=headers,cookies=cookies)
    return response.content
def get_media_page(user_id,end_token):
        
    variables = '{"id":"' + user_id + '","first":12,"after":"' + end_token + '"}'
    url = "https://www.instagram.com/graphql/query/?query_hash=02e14f6a7812a876f7d133c9555b1151&variables="+variables
    response =  requests.get(url,headers==headers,cookies=cookies)
    return response.content
def get_stories_info_page(user):  

    response = requests.get('https://www.instagram.com/stories/'+user+'/?__a=1',headers=headers,cookies=cookies)
    return response.content

def get_stories_page(reels_id):
    response = requests.get('https://i.instagram.com/api/v1/feed/reels_media/?reel_ids='+str(reels_id),cookies=cookies,headers=headers)
    return response.content


