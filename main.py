
import getpage
import scrapepage
import downloader
import json
end_token = ''
page = getpage.get_info_page('renatogarciayt')

id = scrapepage.get_id(page)
total = scrapepage.get_total_posts(page)
media_name = 1


def scrape_media(end_token):
    global media_name 

    # Faz a requisição da pagina
    obj_json = getpage.get_media_page(id,end_token)
    #Pega a resposta e carrega o json
    obj_json = json.loads(obj_json)
    #Acessa os posts
    vet_posts = scrapepage.get_timeline(obj_json)
    lista = []
    lista = scrapepage.nav_timeline(vet_posts)
    for i in lista:
        print('Baixando '+str(media_name)+"/"+str(total))  
        url = scrapepage.get_image_link(i)
        downloader.download(url,media_name,'.jpeg','downloads')
        media_name = media_name+1
    #Verifica se há uma próxima pagina 
    token = scrapepage.has_next_page(obj_json)
    #Se tiver acessa a proxima pagina chamando a funçao novamente com o token da mesma 
    if token != 0:
        print('Acesando proxima página!')
        end_token = token
        scrape_media(token)
    #Caso contrario termina o programa
    else:
        print("Download terminou!")
        return

while True:
    scrape_media(end_token)


stories_info_page = getpage.get_stories_info_page('doarda')
reels_id = scrapepage.get_reels_id(stories_info_page)

def scrape_stories(reels_id):
    cont = 0
    nome = 1
    stories_page = getpage.get_stories_page(reels_id)
    obj_json = scrapepage.get_stories_timeline(stories_page,reels_id)
    lista = []
    lista =  scrapepage.nav_stories_timeline(obj_json)

    for i in lista:

        if i == 1:
            downloader.download(lista[cont+1],cont-1,'.jpeg','stories')
        elif i == 2:
            downloader.download(lista[cont+1],cont-1,'.mp4','stories')
        cont = cont+1


#scrape_stories(reels_id)


