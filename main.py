import requests
from bs4 import BeautifulSoup

url = "https://tribunademinas.com.br/noticias/politica"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    manchetes = soup.find_all('h2', class_='title')
    paragrafos = soup.find_all('p', class_='excerpt')
    datas = soup.find_all('p', class_='date')

    for i in range(min(len(manchetes), len(paragrafos))):
        manchete = manchetes[i]
        corpo = paragrafos[i]
        data = datas[i]

        if manchete and corpo:
            print(manchete.text)
            print(corpo.text)
            print(data.text)
            print("\n----------------------------------------------------\n")
else:
    print("Falha ao obter a página. Código de status:", response.status_code)
