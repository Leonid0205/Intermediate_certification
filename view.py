import json
from datetime import datetime as dt
from checks import check_length_title, check_length_content

def get_value():
    with open('note_directory.json', 'r', encoding='utf-8') as n_d:
        note_dir_test = json.load(n_d)
        if note_dir_test == []:
            length = 0
        else: 
            length1 = note_dir_test[0]['id']
            for n in note_dir_test:
                if n['id'] > length1:
                    length = n['id']
                    length1 = length
    note_dir = {}
    note_dir['id'] = int(length) + 1
    note_dir['title'] = check_length_title('title')
    note_dir['content'] = check_length_content('content')
    note_dir['create date'] = dt.now().strftime('%Y-%M-%D %H:%M:%S')
    return note_dir
def show_note(list):
    for n, i in enumerate(list):
        print('---------------------------------------')
        print(f'{n + 1} Note\n'
              f'id: {i["id"]}\n'
              f'title: {i["title"]}\n'
              f'content: {i["content"]}\n'
              f'create date: {i["create date"]}')
        print('---------------------------------------')
def show_note_dir():
    with open('note_directory.json', 'r', encoding='utf-8') as n_d:
        note_dir = json.load(n_d)
        if note_dir == []:
            print('\nNotes directore is empty')
        else:
            print('\nThe following notes found: \n')
            for n, i in enumerate(note_dir):
                print(f'{n + 1} Note\n'
                f'id: {i["id"]}\n'
                f'title: {i["title"]}\n'
                f'content: {i["content"]}\n'
                f'create date: {i["create date"]}\n')