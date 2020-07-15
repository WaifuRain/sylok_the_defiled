"""
non kanji title - <span class="h1-title">
kanji - <div class="normal-header" style="height: 15px;">
            <span style="font-weight: normal;">
description - <td valign="top" style="padding-left: 5px;">
voice actors - [all] <table border="0" cellpadding ="0" cellspacing="0" width="100%">
                        <tbody>
                            <tr>
                                <td class="borderClass" valign="top">
                                    <a>
voice actor language -          <div style="margin-top: 2px;">
                                    <small>
animeography - <div id="content">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                        <tbody>
                            [all] <tr>
                                    <td valign="top" class="borderClass">
                                        <a>
mangaography - same as animeography
"""

import requests
from bs4 import BeautifulSoup


class Character:
    def __init__(self, character_id):
        self.character_id = character_id
        self.source = requests.get(f'https://myanimelist.net/character/{str(character_id)}').text
        self.name = self.get_name()
        self.kanji = self.get_kanji()
        self.description = self.get_description()
        self.voice_actors = self.get_voice_actors()
        self.animeography = self.get_animeography()
        self.mangaography = self.get_mangaography()
        self.image_list = self.get_image_list()
        self.voice_actor_languages = self.get_voice_actor_languages()
        self.actors = self.compile_voice_actor_list()

    def get_name(self):
        soup = BeautifulSoup(self.source, features='html.parser')
        name = soup.find('span', class_='h1-title')
        return name.text.replace('  ', ' ')

    def get_kanji(self):
        soup = BeautifulSoup(self.source, features='html.parser')
        kanji = soup.find('div', class_='normal_header', style='height: 15px;')
        kanji = kanji.find_next('span', style='font-weight: normal;')
        return kanji.text

    def get_description(self):
        soup = BeautifulSoup(self.source, features='html.parser')
        description = soup.find('td', valign='top', style='padding-left: 5px;')
        description = description.text[description.text.find(')') + 1:description.text.find('Voice Actors')]
        return description.strip()

    def get_voice_actors(self):
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
            if item == 'See More':
                break
            else:
                actor_list.append(item)
        return actor_list

    def get_voice_actor_languages(self):
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

    def compile_voice_actor_list(self):
        complete_list = []
        for i in range(len(self.voice_actors)):
            x, y = self.voice_actors[i], self.voice_actor_languages[i]
            complete_list.append((x, y))
        return complete_list

    def get_animeography(self):
        pass  # TODO

    def get_mangaography(self):
        pass  # TODO

    def get_image_list(self):
        pass  # TODO
