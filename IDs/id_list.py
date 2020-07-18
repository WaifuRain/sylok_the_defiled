def file_len(fname):
    with open(fname, encoding='utf-8') as fp:
        for i, l in enumerate(fp):
            pass
    return i + 1


def id_list():
    character_id_list = []
    with open('valid_id_list_new.txt', 'r', encoding='utf-8') as f:
        for i in range(file_len('valid_id_list_new.txt')):
            line = f.readline()
            character_id = line[line.find(':')+1:line.find('name')].strip()
            character_id_list.append(character_id)
    return character_id_list
