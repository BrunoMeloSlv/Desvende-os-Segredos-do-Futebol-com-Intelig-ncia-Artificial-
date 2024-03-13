import requests 
import pandas as pd
from bs4 import BeautifulSoup

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'} 
request = requests.get('https://www.footstats.com.br/#/ranking/jogadores/803', headers=header)

if request.status_code == 200:
    print('ok')
    content = request.content
    soup = BeautifulSoup(content, 'html.parser')
    dados = soup.find(name="table")
    print(dados)