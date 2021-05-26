import requests


headers = { 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57'}
cookies = {'sessionid':'2113549053%3AkNItZ2yWAfCTYa%3A13'}

def get_page(user):  

    response = requests.get('https://www.instagram.com/'+user+'/?__a=1',headers=headers,cookies=cookies)
    return response.content
def get_next_page(user_id,end_token):
        
    variables= '{"id":"' + user_id + '","first":12,"after":"' + end_token + '"}'
    url = "https://www.instagram.com/graphql/query/?query_hash=02e14f6a7812a876f7d133c9555b1151&variables="+variables
    response =  requests.get(url,headers==headers,cookies=cookies)
    return response.content




