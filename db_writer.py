import os
from waifu_db import waifu_db as db

root_directory = 'C:\\Users\\bridg\\Desktop\\Rain Drive\\stuff\\Waifu Database'
os.chdir(root_directory)
for character_id in db:
    os.chdir(root_directory)
    os.mkdir(character_id)
    os.chdir(f'{root_directory}\\{character_id}')
    with open(f'name.txt', 'w', encoding='utf-8') as name:
        name.write(db[character_id]['name'])
    with open(f'description.txt', 'w', encoding='utf-8') as description:
        description.write(db[character_id]['description'])

"""
todo: write images to the waifu database

"""

