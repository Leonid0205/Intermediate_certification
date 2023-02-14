import json
from checks import check_id

def search_note(n):
    with open('note_directory.json', 'r', encoding='utf-8') as n_d:
        note_dir = json.load(n_d)
        search_contact_res = []
        if n == 1:
            id = check_id()
            for i in note_dir:
                if i['id'] == id:
                    search_contact_res.append(i)
            return search_contact_res
        if n == 2:
            title = input('Input title name: ')
            for i in note_dir:
                if i['title'] == title:
                    search_contact_res.append(i)
            return search_contact_res
        elif n == 3:
            contetnt = input('Input content: ')
            for i in note_dir:
                if i['content'] == contetnt:
                    search_contact_res.append(i)
            return search_contact_res