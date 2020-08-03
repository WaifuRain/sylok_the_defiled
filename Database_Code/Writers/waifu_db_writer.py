import os
import requests
from Database_Code.Databases.waifu_db import waifu_db as db
from tqdm import tqdm


root_directory = 'E:\\Waifu Database'
os.chdir(root_directory)

for character_id in tqdm(db):
    try:
        img_count = 0
        nick_count = 0
        actor_count = 0
        os.chdir(root_directory)
        os.mkdir(character_id)
        os.chdir(f'{root_directory}\\{character_id}')
        os.mkdir('info')
        os.chdir(f'{root_directory}\\{character_id}\\info')
        with open(f'name.txt', 'w', encoding='utf-8') as name:
            name.write(db[character_id]['info']['name'])
        with open(f'kanji.txt', 'w', encoding='utf-8') as kanji:
            kanji.write(db[character_id]['info']['kanji'])
        os.mkdir('nicknames')
        os.chdir(f'{root_directory}\\{character_id}\\info\\nicknames')
        for names in db[character_id]['info']['nicknames']:
            nick_count += 1
            with open(f'nicknames {nick_count}.txt', 'w', encoding='utf-8') as nickname:
                nickname.write(names)
        os.chdir(f'{root_directory}\\{character_id}\\info')
        with open(f'initials.txt', 'w', encoding='utf-8') as initials:
            initial_string = ''
            for inital in db[character_id]['info']['initials']:
                initial_string += f'{inital}. '
            initials.write(initial_string.strip())
        try:
            with open(f'description.txt', 'w', encoding='utf-8') as description:
                description.write(db[character_id]['info']['description'])
        except UnicodeEncodeError:
            with open(f'description.txt', 'w', encoding='utf-16') as description:
                description.write(db[character_id]['info']['description'])
        os.chdir(f'{root_directory}\\{character_id}')
        os.mkdir('images')
        os.chdir(f'{root_directory}\\{character_id}\\images')
        for image in db[character_id]['images']:
            img_count += 1
            image_data = requests.get(image).content
            with open(f'{img_count}.jpg', 'wb') as img:
                img.write(image_data)
        os.mkdir('links')
        os.chdir(f'{root_directory}\\{character_id}\\images\\links')
        link_count = 0
        for link in db[character_id]['images']:
            link_count += 1
            with open(f'link_{link_count}.txt', 'w') as links:
                links.write(link)
        os.chdir(f'{root_directory}\\{character_id}')
        os.mkdir('appearances')
        os.chdir(f'{root_directory}\\{character_id}\\appearances')
        os.mkdir('anime')
        os.mkdir('manga')
        os.chdir(f'{root_directory}\\{character_id}\\appearances\\anime')
        anime_string = ''
        for anime in db[character_id]['appearances']['animeography']:
            anime_string += f'{anime}\n'
        with open(f'anime.txt', 'w', encoding='utf-8') as anime:
            anime.write(anime_string)
        os.chdir(f'{root_directory}\\{character_id}\\appearances\\manga')
        manga_string = ''
        for manga in db[character_id]['appearances']['mangaography']:
            manga_string += f'{manga}\n'
        with open(f'manga.txt', 'w', encoding='utf-8') as manga:
            manga.write(manga_string)
        os.chdir(f'{root_directory}\\{character_id}')
        os.mkdir('actors')
        os.chdir(f'{root_directory}\\{character_id}\\actors')
        for actors in db[character_id]['actors']:
            actor_count += 1
            actor_string = ''
            actor_string += f'name: {actors[0].split(",")[-1]} {actors[0].split(",")[0]}\nlanguage: {actors[1]}'
            with open(f'{actor_count}.txt', 'w', encoding='utf-8') as actor:
                actor.write(actor_string.strip())
    except FileExistsError:
        pass
