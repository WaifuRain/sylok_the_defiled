from bs4 import BeautifulSoup
import requests


def get_image(character_id):
    source = requests.get(f'https://myanimelist.net/character/{character_id}').text
    soup = BeautifulSoup(source, features='html.parser')
    waifu = soup.find('img', class_='lazyload')
    image = str(waifu)
    image = image[image.find('https'):image.find('jpg') + 3]
    return image
