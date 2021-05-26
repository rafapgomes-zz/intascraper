import requests

from pathlib import Path
pasta = Path('downloads')

def download(url,name):
    response = requests.get(url)
    arq = str(name) + '.jpeg'
    with (pasta/arq).open("wb") as f:
            f.write(response.content)
    f.close()

    tamanho = Path('downloads/'+str(name)+'.jpeg').stat().st_size
    if tamanho == 0:
        print("Download falhou, tentando novamente")
        download(url,name)
    print('Download completo')

   