from bs4 import BeautifulSoup
import getpage
import json

def get_id(page):

        obj_json = json.loads(page)
        id = obj_json['logging_page_id']
        return id[12:]

def get_reels_id(page):
    obj_json = json.loads(page)
    return obj_json['user']['id']

def get_stories_timeline(page,reels_id):
    obj_json = json.loads(page)
    return obj_json['reels'][str(reels_id)]['items']

def nav_stories_timeline(obj_json):
    lista = []
    for item in obj_json:
        if item['media_type'] == 1:
            lista.append(1)
            lista.append(item['image_versions2']['candidates'][0]['url'])
        elif item['media_type'] == 2:
            lista.append(2)
            lista.append(item['video_versions'][0]['url'])
    return lista

def has_next_page(json):
    if json['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page'] == True:
        return json['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    else:
        return 0

def get_total_posts(page):
    obj_json = json.loads(page)

    return obj_json['graphql']['user']['edge_owner_to_timeline_media']['count']

def get_timeline(obj_json):
    vet_posts = obj_json['data']['user']['edge_owner_to_timeline_media']['edges']
    return vet_posts    



def nav_timeline(vet_posts):
    lista = []
    for post in vet_posts:
        
        if getypename(post)== 'GraphSidecar':
            sidecar = post['node']['edge_sidecar_to_children']['edges']
            for item in sidecar:
                if getypename(item) != 'GraphVideo':
                   lista.append(item)
        elif getypename(post) == 'GraphImage':
            lista.append(post)
            
    return lista
                
def get_image_link(post):
    return (post['node']['display_url'])

def getypename(post):
    return post['node']['__typename']



    

