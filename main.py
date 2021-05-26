
import getpage
import scrapepage
import downloader
end_token = ''
page = getpage.get_page('renatogarciayt')

id = scrapepage.get_id(page)
total = scrapepage.get_total_posts(page)
print(total)
nome = 1



def main(end_token):
    global nome
    # Faz a requisição da pagina
    obj_json = getpage.get_next_page(id,end_token)
    #Pega a resposta e carrega o json
    obj_json = scrapepage.get_json(obj_json)
    #Acessa os posts
    vet_posts = scrapepage.get_timeline(obj_json)
    lista = []
    lista = scrapepage.nav_timeline(vet_posts)
    for i in lista:
        print('Baixando '+str(nome)+"/"+str(total))  
        url = scrapepage.get_image_link(i)
        downloader.download(url,nome)
        nome = nome+1
    #Verifica se há uma próxima pagina 
    token = scrapepage.has_next_page(obj_json)
    #Se tiver acessa a proxima pagina chamando a funçao novamente com o token da mesma 
    if token != 0:
        print('Acesando proxima página!')
        end_token = token
        main(token)
    #Caso contrario termina o programa
    else:
        print("Download terminou!")
        return

main(end_token)