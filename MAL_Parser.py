import requests
from bs4 import BeautifulSoup


class Character:
    def __init__(self, character_id):
        self.character_id = character_id
        self.source = requests.get(f'https://myanimelist.net/character/{str(character_id)}').text
        self.name = self.get_name()
        self.first = self.name.split(' ')[0]
        self.last = self.name.split(' ')[-1]
        self.kanji = self.get_kanji()
        self.description = self.get_description()
        self.voice_actors = self.get_voice_actors()
        self.animeography = self.get_animeography_and_mangaography('A')
        self.mangaography = self.get_animeography_and_mangaography('M')
        self.images = self.get_image_list()
        self.voice_actor_languages = self.get_voice_actor_languages()
        try:
            self.actors = list(zip(self.voice_actors, self.voice_actor_languages))
        except TypeError:
            self.actors = []
        self.initials = self.get_initials()
        self.nicknames = self.get_nicknames()
        if '"' in self.name:
            self.database_name = self.name[:self.name.find('"')] + self.name[self.name.find('" ') + 1:].strip()
        else:
            self.database_name = self.name.strip()

    def get_name(self):
        soup = BeautifulSoup(self.source, features='html.parser')
        name = soup.find('span', class_='h1-title')
        return name.text.replace('  ', ' ')

    def get_kanji(self):
        try:
            soup = BeautifulSoup(self.source, features='html.parser')
            kanji = soup.find('div', class_='normal_header', style='height: 15px;')
            kanji = kanji.find_next('span', style='font-weight: normal;')
            return kanji.text
        except AttributeError:
            return ''

    def get_description(self):
        soup = BeautifulSoup(self.source, features='html.parser')
        description = soup.find('td', valign='top', style='padding-left: 5px;')
        description = description.text[description.text.find(')') + 1:description.text.find('Voice Actors')]
        return description.strip()

    def get_voice_actors(self):
        try:
            soup = BeautifulSoup(self.source, features='html.parser')
            voice_actors = soup.find('td', valign='top', style='padding-left: 5px;')
            voice_actors = voice_actors.find_next('table', border='0', cellpadding='0', cellspacing='0', width='100%')
            voice_actors = voice_actors.find_all_next('a', text=True)
            temp_list = []
            actor_list = []
            for actor in voice_actors:
                actor = str(actor)
                actor = actor[actor.find('">')+2:actor.find('</a>')]
                temp_list.append(actor)
            for item in temp_list:
                if item == 'See More' or item == 'More':
                    break
                else:
                    actor_list.append(item)
            return actor_list
        except AttributeError:
            return None

    def get_voice_actor_languages(self):
        try:
            soup = BeautifulSoup(self.source, features='html.parser')
            languages = soup.find('td', valign='top', style='padding-left: 5px;')
            languages = languages.find_next('table', border='0', cellpadding='0', cellspacing='0', width='100%')
            languages = languages.find_all_next('small', text=True)
            language_list = []
            for language in languages:
                language = str(language)
                language = language[language.find('>') + 1:language.find('</small>')]
                language_list.append(language)
            return language_list
        except AttributeError:
            return None

    def get_animeography(self):
        animeography = []
        soup = BeautifulSoup(self.source, features='html.parser')
        soup = soup.find('div', id='myanimelist').find('div', class_='wrapper').find('div', id='contentWrapper').find('div', id='content')
        soup = soup.find('table', border='0', cellpadding='0', cellspacing='0', width='100%')
        soup = soup.find('td', width='225', class_='borderClass', style='border-width: 0 1px 0 0;', valign='top')
        soup = soup.find('table', border='0', cellpadding='0', cellspacing='0', width='100%')
        soup = soup.find_all('a', href=True, class_=False, title=False, text=True)
        for anime in soup:
            anime = str(anime)
            animeography.append(anime[anime.find('">') + 2:anime.find('</a>')])
        return animeography

    def get_animeography_and_mangaography(self, type_of_content):
        animeography = []
        mangaography = []
        soup = BeautifulSoup(self.source, features='html.parser')
        soup = soup.find('div', id='myanimelist').find('div', class_='wrapper').find('div', id='contentWrapper').find('div', id='content')
        soup = soup.find('table', border='0', cellpadding='0', cellspacing='0', width='100%')
        soup = soup.find('td', width='225', class_='borderClass', style='border-width: 0 1px 0 0;', valign='top')
        soup = soup.find_all('table', border='0', cellpadding='0', cellspacing='0', width='100%')
        t = []
        for tag in soup:
            t.append(tag.find_all('a', href=True, class_=False, title=False, text=True))
        if type_of_content == 'A':
            for animes in t[0]:
                animes = str(animes)
                animeography.append(animes[animes.find('">') + 2:animes.find('</a>')])
            return animeography
        elif type_of_content == 'M':
            for mangas in t[1]:
                mangas = str(mangas)
                mangaography.append(mangas[mangas.find('">') + 2:mangas.find('</a>')])
            return mangaography

    def get_image_list(self):
        image_list = []
        soup = BeautifulSoup(requests.get(f'https://myanimelist.net/character/{self.character_id}/{self.first}_{self.last}/pictures').text, features='html.parser')
        soup = soup.find_all('a', href=True, title=True, class_='js-picture-gallery', rel='gallery-character')
        for link in soup:
            link = str(link)
            link = link[link.find('https://'):link.find('.jpg') + 4]
            image_list.append(link)
        image_list = set(image_list)
        return list(image_list)

    def get_initials(self):
        try:
            if '"' in self.name:
                return [name[0] for name in (self.name[:self.name.find('"')] + self.name[self.name.find('" ') + 1:]).replace('  ', ' ').split(' ')]
            else:
                return [name[0] for name in self.name.split(' ')]
        except IndexError:
            return self.name[0]

    def get_nicknames(self):
        nickname_list = []
        if '"' in self.name:
            for nicknames in self.name[self.name.find('"') + 1:self.name.find('" ')].split(','):
                nickname_list.append(nicknames.strip())
            return nickname_list
        else:
            return []


class Anime:
    pass


class Manga:
    pass
