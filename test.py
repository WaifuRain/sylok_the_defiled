# from get_attributes import Character
#
# test_waifu = Character(533)
# print(test_waifu.first)
# print(test_waifu.description)

from MAL_Parser import Character

test_waifu = Character(1)
print(test_waifu.name)
print(test_waifu.kanji)
print(test_waifu.description)
print(test_waifu.actors)
