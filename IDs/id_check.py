from bs4 import BeautifulSoup
import requests
from time import sleep
from IDs.id_list import id_list
# import id_list
from exceptions import HeavyAccessRestrictionError

current_id = int(id_list()[-1])
# current_id = 0
valid_ids = []
invalid_ids = 0
number_of_requests = 0
total_requests = 0
count_requests = 0
total_valid_ids = 0


def write_ids(character_id_list):  # append valid ids to file every 100 requests
    print('Writing valid ids...')
    with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\IDs\\valid_id_list_new.txt', 'a', encoding='utf-8') as f:
        for data in character_id_list:
            character_id = data
            f.write(f'id:{character_id}\n')


while True:
    current_id += 1
    print(f'\nvalid_ids: {total_valid_ids}/{count_requests}')

    if total_requests >= 100:
        write_ids(valid_ids)
        valid_ids = []
        total_requests = 0

    if number_of_requests == 10:
        sleep(2.5)
        number_of_requests = 0

    source = requests.get(f'https://myanimelist.net/character/{current_id}').text
    number_of_requests += 1
    total_requests += 1
    count_requests += 1
    soup = BeautifulSoup(source, features='html.parser')

    if soup.find('div', class_='caption') is None:
        pass
    else:
        write_ids(valid_ids)
        raise HeavyAccessRestrictionError

    for content_wrapper in soup.find_all('div', id='contentWrapper'):
        h1 = content_wrapper.div.h1.text
        if h1 != 'Invalid':
            total_valid_ids += 1
            valid_ids.append(current_id)
        else:
            print(f'id: {current_id}\nstate: Invalid\noutput: {h1}')
            invalid_ids += 1
