import json

def delete_note(list):
    with open('note_directory.json', 'r', encoding='utf-8') as n_d:
        note_dir = json.load(n_d)
    for i in range(len(note_dir)):
        if note_dir[i] == list[0]:
            note_dir.pop(i)
            break           
    with open('note_directory.json', 'w', encoding='utf-8') as n_d:
        json.dump(note_dir, n_d, indent=2)
    print('\nThe note is succesfully deleted')