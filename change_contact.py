import json
import checks

def note_change(list):
    with open('note_directory.json', 'r', encoding='utf-8') as n_d:
        note_dir = json.load(n_d)
    for i in range(len(note_dir)):
        if note_dir[i] == list[0]:
            print('What you want to change: \n'
                '1 - Title\n'
                '2 - Content\n')
            change = checks.check(4)
            if change == 1:
                note_dir.pop(i)
                list[0]['title'] = checks.check_length_title('title')
                note_dir.append(list[0])
                break
            if change == 2:
                note_dir.pop(i)
                list[0]['content'] = checks.check_length_content('Content')
                note_dir.append(list[0])
                break
    with open('note_directory.json', 'w', encoding='utf-8') as n_d:
        json.dump(note_dir, n_d, indent=2)
    print('\nThe note is changed')