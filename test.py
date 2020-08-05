# from get_attributes import Character
#
# test_waifu = Character(533)
# print(test_waifu.first)
# print(test_waifu.description)

# from MAL_Parser import Character, OldCharacter
# import time

# start = time.time()
# test_waifu = Character(11)
# print(test_waifu.name)
# print(test_waifu.database_name)
# print(test_waifu.nicknames)
# print(test_waifu.kanji)
# print(test_waifu.images)
# print(test_waifu.description)
# print(test_waifu.actors)
# print(test_waifu.animeography)
# print(test_waifu.animeography)
# stop = time.time()
# print(stop - start)
#
# start = time.time()
# test_waifu = OldCharacter(11)
# print(test_waifu.name)
# print(test_waifu.database_name)
# print(test_waifu.nicknames)
# print(test_waifu.kanji)
# print(test_waifu.images)
# print(test_waifu.description)
# print(test_waifu.actors)
# print(test_waifu.animeography)
# print(test_waifu.animeography)
# stop = time.time()
# print(stop - start)


# import os
# import random
# waifu_database_root = 'E:\\Waifu Database'
#
#
# root, waifu = next(os.walk(waifu_database_root))[0], random.choice(next(os.walk(waifu_database_root))[1])
# print(waifu)
# print(f'{root}\\{waifu}\\info')
# print(f'{root}\\{waifu}\\actors')
# print(f'{root}\\{waifu}\\appearances\\anime')
# print(f'{root}\\{waifu}\\appearances\\manga')
# print(f'{root}\\{waifu}\\images')
# print(f'{root}\\{waifu}\\nicknames')

from Database_Code.Databases.waifu_db import waifu_db

true_count = 0
count = 0
# print(waifu_db.keys())
for key in waifu_db.keys():
    true_count += 1
    if 'No biography written.' in waifu_db[key]['info']['description']:
        count += 1
        # print(key)
print(f'Bad descriptions: {count}/{true_count}')  # bad descriptions: 7744/43558, 17.78%

true_count = 0
count = 0
# print(waifu_db.keys())
for key in waifu_db.keys():
    true_count += 1
    if not waifu_db[key]['images']:
        count += 1
        # print(key)
print(f'Bad image lists: {count}/{true_count}')  # empty image lists: 1954/43558, 4.49%

# for character_id in waifu_db.keys():
#     if 'No biography written.' in waifu_db[character_id]['info']['description']:
#         pass
#     if 'DetailsPictures' in waifu_db[character_id]['info']['description'] and 'No biography written.' not in waifu_db[character_id]['info']['description']:
#         print(waifu_db[character_id]['info']['description'])
#         print('\n')
#         print(waifu_db[character_id]['info']['description'][waifu_db[character_id]['info']['description'].rfind(' \n'):])
#         print('\n\n\n')
