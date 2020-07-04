from get_attributes import Character
import json
import id_list as id_lst
from waifu_db import waifu_db
"""
Check the name of id:620 in the waifu database

"""


def count_lines(file):
    lines = 0
    with open(file) as f:
        for j in range(int(id_lst.id_list()[-1])):
            if f.readline() is not '':
                lines += 1
    return lines


with open('valid_id_list_new.txt', 'r') as id_list:
    character_id_list = []
    for i in range(count_lines('valid_id_list_new.txt')):
        id_string = id_list.readline().strip()
        character_id_list.append(id_string[id_string.find(":")+1:])

new_dictionary = waifu_db
for waifu_id in character_id_list:
    w = Character(waifu_id)
    new_dictionary.update({w.character_id: {'name': w.name, 'description': w.description, 'images': w.images}})

    with open('waifu_db.py', 'w') as db:
        db.write(f'waifu_db = {json.dumps(new_dictionary, indent=2)}')
        print(f"Waifu '{w.name}' written to database.")
