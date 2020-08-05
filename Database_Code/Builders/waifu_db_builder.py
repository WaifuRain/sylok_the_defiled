from MAL_Parser import Character
import json
from IDs.id_list import id_list as id_lst
import time
from tqdm import tqdm
# import id_list as id_lst
import exceptions


def count_lines(file):
    lines = 0
    with open(file) as f:
        for j in range(int(max(id_lst()))):
            if f.readline() is not '':
                lines += 1
    return lines


with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\Database_Code\\Databases\\waifu_db.py', 'r') as check:
    if check.read() == '':
        with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\Database_Code\\Databases\\waifu_db.py', 'w') as waifu_db:
            waifu_db.write('waifu_db = {}\n')

with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\IDs\\valid_id_list_new.txt', 'r') as id_list:
    character_id_list = []
    for i in range(count_lines('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\IDs\\valid_id_list_new.txt')):
        id_string = id_list.readline().strip()
        character_id_list.append(id_string[id_string.find(":")+1:])

from Database_Code.Databases.waifu_db import waifu_db
new_dictionary = waifu_db
scraping_error_count = 0
# print(character_id_list)
# print(waifu_db.keys())
for waifu_id in tqdm(character_id_list):
    if waifu_id in waifu_db.keys():
        pass
    else:
        time.sleep(2.5)
        try:
            w = Character(waifu_id)
        except exceptions.MALScrapingError:
            scraping_error_count += 1
            print(f"Sleeping for 10 minutes. Error count: {scraping_error_count}")
            time.sleep(600)
        new_dictionary.update({w.character_id: {
            'info': {
                'name': w.database_name.strip(), 'kanji': w.kanji, 'nicknames': w.nicknames, 'initials': w.initials, 'description': w.description.strip()},
                'images': w.images,
                'appearances': {'animeography': w.animeography, 'mangaography': w.mangaography},
                'actors': w.actors}
            })

        with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\Database_Code\\Databases\\waifu_db.py', 'w') as db:
            db.write(f'waifu_db = {json.dumps(new_dictionary, indent=4)}')
            # print(f"Waifu '{w.name}', id:{w.character_id} written to database.")
