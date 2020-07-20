from MAL_Parser import Character
import json
from IDs.id_list import id_list as id_lst
import time
# import id_list as id_lst


def count_lines(file):
    lines = 0
    with open(file) as f:
        for j in range(int(id_lst()[-1])):
            if f.readline() is not '':
                lines += 1
    return lines


with open('../Databases/waifu_db.py', 'r') as check:
    if check.read() == '':
        with open('../Databases/waifu_db.py', 'w') as waifu_db:
            waifu_db.write('waifu_db = {}\n')

with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\bot\\IDs\\valid_id_list_new.txt', 'r') as id_list:
    character_id_list = []
    for i in range(count_lines('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\bot\\IDs\\valid_id_list_new.txt')):
        id_string = id_list.readline().strip()
        character_id_list.append(id_string[id_string.find(":")+1:])

from Database_Code.Databases.waifu_db import waifu_db
new_dictionary = waifu_db
for waifu_id in character_id_list:
    if waifu_id in waifu_db.keys():
        pass
    else:
        time.sleep(5)
        w = Character(waifu_id)
        new_dictionary.update({w.character_id: {
            'info': {
                'name': w.database_name.strip(), 'kanji': w.kanji, 'nicknames': w.nicknames, 'initials': w.initials, 'description': w.description},
                'images': w.images,
                'appearances': {'animeography': w.animeography, 'mangaography': w.mangaography},
                'actors': w.actors}
            })

        with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\bot\\Database_Code\\Databases\\waifu_db.py', 'w') as db:
            db.write(f'waifu_db = {json.dumps(new_dictionary, indent=4)}')
            print(f"Waifu '{w.name}' written to database.")
