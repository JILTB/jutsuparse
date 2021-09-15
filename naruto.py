import requests
from bs4 import BeautifulSoup
import time

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3;q=0.9'}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('span', id='wap_player_2')
    for item in items:
        naruto = item.get('data-player-480')
    return naruto


def download():
    for i in range(1, 221):
        URL = f'https://jut.su/narutoo/season-1/episode-{i}.html'
        html = get_html(URL)
        time.sleep(5)
        if html.status_code == 200:
            download_url = get_content(html.text)
        down = get_html(download_url)
        if down.status_code == 200:
            with open(f'C:\\Users\\Ivan-\\PycharmProjects\\jutsuparse\\series\\{i}.mp4', 'wb') as f:
                f.write(down.content)
            print(f'Скачал Серию {i}')
        else:
            print(f'Ошибка, Серия {i} не скачалась')


download()
