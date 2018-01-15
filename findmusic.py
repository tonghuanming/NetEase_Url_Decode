from bs4 import BeautifulSoup
import requests
import random

listurl = 'http://music.163.com/discover/playlist?order=new&limit=1&offset=%d'
songurl = 'http://music.163.com%s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4630.400 QQBrowser/10.0.520.400',
    'Host': 'music.163.com',
    'Referer': 'http://music.163.com/'
}


def getplaylist():
    lurl = listurl % random.randint(0, 3000)
    web_data = requests.get(listurl, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    playlist = soup.select('a.msk')[0].get('href')
    return playlist


def getmusic():
    url = songurl % getplaylist()
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    music = soup.select('#song-list-pre-cache > ul > li > a')
    musicurl = music[random.randint(0, len(music))].get('href')
    return musicurl
