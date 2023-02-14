import json

def create_note_directory(list):
    try:
        with open('note_directory.json', 'r', encoding='utf-8') as n_d:
            note_dir = json.load(n_d)
    except:
            note_dir = []
    note_dir.append(list)
    with open('note_directory.json', 'w', encoding='utf-8') as n_d:
        json.dump(note_dir, n_d, indent = 2)
        print('\nContact is successfully added\n')