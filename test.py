# from get_attributes import Character
#
# test_waifu = Character(533)
# print(test_waifu.first)
# print(test_waifu.description)

from MAL_Parser import Character
from waifu_db import waifu_db

test_waifu = Character(11)
print(test_waifu.name.strip())
print(test_waifu.nicknames)
print(test_waifu.database_name)
