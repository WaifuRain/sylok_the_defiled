import os
import requests
from Database_Code.Databases.waifu_db import waifu_db as db

root_directory = 'C:\\Users\\bridg\\Desktop\\Rain Drive\\stuff\\Waifu Database'
os.chdir(root_directory)
for character_id in db:
    img_count = 0
    os.chdir(root_directory)
    os.mkdir(character_id)
    os.chdir(f'{root_directory}\\{character_id}')
    with open(f'name.txt', 'w', encoding='utf-8') as name:
        name.write(db[character_id]['name'])
    with open(f'description.txt', 'w', encoding='utf-8') as description:
        description.write(db[character_id]['description'])
    for image in db[character_id]['images']:
        img_count += 1
        image_data = requests.get(image).content
        with open(f'{img_count}.jpg', 'wb') as img:
            img.write(image_data)
    print(f"{db[character_id]['name']} written to database.")

