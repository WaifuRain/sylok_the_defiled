from bs4 import BeautifulSoup
import requests


class Character:
    """
    Each character should have:
    - Name
    - List of associated Images
    - Description
    - ..
    """

    def __init__(self, character_id):
        self.character_id = character_id
        self.name = self.get_name()
        self.images = self.get_images()
        self.description = self.get_description()

    def get_name(self):
        source = requests.get(f'https://myanimelist.net/character/{self.character_id}').text
        soup = BeautifulSoup(source, features='html.parser')
        name = soup.find('div', style='height: 15px;', class_='normal_header')
        return name.text[:name.text.find('(') - 1]

    def get_images(self):
        image_list = []
        source = requests.get(f'https://myanimelist.net/character/{self.character_id}/{self.name[:self.name.find(" ")]}_{self.name[self.name.find(" ") + 1:]}/pictures').text
        soup = BeautifulSoup(source, features='html.parser')
        for images in soup.find_all('img', alt=self.name, class_='lazyload'):
            image_source = str(images)
            image_list.append(image_source[image_source.find('https'):image_source.find('jpg') + 3])
        return image_list

    def get_description(self):
        source = requests.get(f'https://myanimelist.net/character/{self.character_id}').text
        soup = BeautifulSoup(source, features='html.parser')
        description = soup.find('td', valign='top', style='padding-left: 5px;')
        try:
            description = description.br.text[:description.br.text.find('Voice Actors')]
        except AttributeError:
            return ''
        return description.strip()


# character = Character(2)
# print(character.images)
# print(f'{character.name[:character.name.find(" ")]}_{character.name[character.name.find(" ") + 1:]}')
# print(character.images)
# print(character.description)
