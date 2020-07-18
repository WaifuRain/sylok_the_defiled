from MAL_Parser import Character
import json
import id_list as id_lst


def count_lines(file):
    lines = 0
    with open(file) as f:
        for j in range(int(id_lst.id_list()[-1])):
            if f.readline() is not '':
                lines += 1
    return lines


with open('waifu_db.py', 'r') as check:
    if check.read() == '':
        with open('waifu_db.py', 'w') as waifu_db:
            waifu_db.write('waifu_db = {}\n')

with open('valid_id_list_new.txt', 'r') as id_list:
    character_id_list = []
    for i in range(count_lines('valid_id_list_new.txt')):
        id_string = id_list.readline().strip()
        character_id_list.append(id_string[id_string.find(":")+1:])

from waifu_db import waifu_db
new_dictionary = waifu_db
for waifu_id in character_id_list:
    if waifu_id in waifu_db.keys():
        pass
    else:
        w = Character(waifu_id)
        new_dictionary.update({w.character_id: {
            'info': {
                'name': w.database_name.strip(), 'kanji': w.kanji, 'nicknames': w.nicknames, 'initials': w.initials, 'description': w.description},
                'images': w.images,
                'appearances': {'animeography': w.animeography, 'mangaography': w.mangaography},
                'actors': w.actors}
            })

        with open('waifu_db.py', 'w') as db:
            db.write(f'waifu_db = {json.dumps(new_dictionary, indent=4)}')
            print(f"Waifu '{w.name}' written to database.")
