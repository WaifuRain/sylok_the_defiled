from bs4 import BeautifulSoup
import requests
from time import sleep
import id_list

current_id = int(id_list.id_list()[-1])
# current_id = 0
valid_ids = []
invalid_ids = 0
number_of_requests = 0
total_requests = 0
count_requests = 0
total_valid_ids = 0


def write_ids(id_list):  # append valid ids to file every 100 requests
    print('Writing valid ids...')
    with open('valid_id_list_new.txt', 'a', encoding='utf-8') as f:
        for data in id_list:
            character_id = data
            f.write(f'id:{character_id}\n')


while True:
    current_id += 1
    print(f'\nvalid_ids: {total_valid_ids}/{count_requests}')

    if total_requests >= 100:
        write_ids(valid_ids)
        valid_ids = []
        total_requests = 0

    if number_of_requests == 25:
        sleep(1)
        number_of_requests = 0

    source = requests.get(f'https://myanimelist.net/character/{current_id}').text

    #print(source)
    number_of_requests += 1
    total_requests += 1
    count_requests += 1
    soup = BeautifulSoup(source, features='html.parser')

    if soup.find('div', class_='caption') is None:
        pass
    else:
        write_ids(valid_ids)
        exit(-1)

    for content_wrapper in soup.find_all('div', id='contentWrapper'):
        h1 = content_wrapper.div.h1.text
        if h1 != 'Invalid':
            total_valid_ids += 1
            # name = h1[h1.find('\n')+1:h1.find('Edit')]
            # if name.find('"') != -1:
            #     name = name[:name.find(' "')] + name[name.find('" ') + 1:]
            # else:
            #     pass
            # valid_ids.append((current_id, name))
            valid_ids.append(current_id)
            # print(f'id: {current_id}\nstate: Valid\noutput: {h1}')
        else:
            print(f'id: {current_id}\nstate: Invalid\noutput: {h1}')
            invalid_ids += 1
