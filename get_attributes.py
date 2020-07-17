from bs4 import BeautifulSoup
import requests

"""
DEPRECATED
"""


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
        self.first = self.name.split(' ')[0]
        self.last = self.name.split(' ')[-1]
        self.description = self.get_description()

    def get_name(self):
        source = requests.get(f'https://myanimelist.net/character/{self.character_id}').text
        soup = BeautifulSoup(source, features='html.parser')
        name = soup.find('div', style='height: 15px;', class_='normal_header')
        return name.text[:name.text.find('(') - 1]

    def get_name_alternate(self):
        source = requests.get(f'https://myanimelist.net/character/{self.character_id}').text
        soup = BeautifulSoup(source, features='html.parser')
        name = soup.find('div', style='height: 15px;', class_='normal_header')
        return name.text[:name.text.find('(')]

    def get_images(self):
        # print(self.name)
        image_list = []
        source = requests.get(f'https://myanimelist.net/character/{self.character_id}/{self.name[:self.name.find(" ")]}_{self.name[self.name.find(" ") + 1:]}/pictures').text
        soup = BeautifulSoup(source, features='html.parser')
        for images in soup.find_all('img', alt=self.name, class_='lazyload'):
            image_source = str(images)
            image_list.append(image_source[image_source.find('https'):image_source.find('jpg') + 3])
        if image_list:
            # print(f'First conditional{image_list}')
            return image_list
        else:
            self.name = self.get_name_alternate()
            self.images = self.get_images()
            # print(f'Second conditional{image_list}')
            return self.images

    def get_description(self):
        source = requests.get(f'https://myanimelist.net/character/{self.character_id}').text
        soup = BeautifulSoup(source, features='html.parser')
        # description = soup.find('td', valign='top', style='padding-left: 5px;')
        description = soup.find_all(string=[self.first, self.last, self.name])
        """
        Still trying to find a way to pull the full description efficiently from waifus, especially id:533
        """
        # try:
        #     description = description.br.text[:description.br.text.find('Voice Actors')]
        # except AttributeError:
        #     return ''
        # return str(description).strip()
        # return soup.get_text()
        return description


# character = Character(2)
# print(character.images)
# print(f'{character.name[:character.name.find(" ")]}_{character.name[character.name.find(" ") + 1:]}')
# print(character.images)
# print(character.description)
