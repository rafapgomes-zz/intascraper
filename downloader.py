import requests

from pathlib import Path
def download(url,name,tipo,file):

    response = requests.get(url)
    arq = str(name) + tipo
    with open(file+'/'+arq,'wb') as f:
            f.write(response.content)
    f.close()
    caminho = file +'/'+ arq
    print(caminho)
    tamanho = Path(caminho).stat().st_size
    print(tamanho)
    if tamanho == 0:
        print("Download falhou, tentando novamente")
        return 
        download(url,name,tipo,file)
    print('Download completo')

        