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

import os
import random
waifu_database_root = 'E:\\Waifu Database'


root, waifu = next(os.walk(waifu_database_root))[0], random.choice(next(os.walk(waifu_database_root))[1])
print(waifu)
print(f'{root}\\{waifu}\\info')
print(f'{root}\\{waifu}\\actors')
print(f'{root}\\{waifu}\\appearances\\anime')
print(f'{root}\\{waifu}\\appearances\\manga')
print(f'{root}\\{waifu}\\images')
print(f'{root}\\{waifu}\\nicknames')
