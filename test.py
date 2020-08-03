# from get_attributes import Character
#
# test_waifu = Character(533)
# print(test_waifu.first)
# print(test_waifu.description)

# from MAL_Parser import Character
#
# test_waifu = Character(11)
# print(test_waifu.name.strip())
# print(test_waifu.nicknames)
# print(test_waifu.database_name)

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

