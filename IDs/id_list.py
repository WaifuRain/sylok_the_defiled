def file_len(fname):
    with open(fname, encoding='utf-8') as fp:
        for i, l in enumerate(fp):
            pass
    return i + 1


def id_list():
    character_id_list = []
    with open('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\IDs\\valid_id_list_new.txt', 'r', encoding='utf-8') as f:
        for i in range(file_len('C:\\Users\\bridg\\PycharmProjects\\sylok_the_defiled\\IDs\\valid_id_list_new.txt')):
            line = f.readline()
            character_id = line[line.find(':')+1:line.find('name')].strip()
            character_id_list.append(int(character_id))
    return character_id_list
