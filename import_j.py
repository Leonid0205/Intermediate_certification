import csv
import json

def import_dir():
    conclusion = []
    with open('note_directory.csv', encoding='utf-8') as n_d_c:
        reader = csv.reader(n_d_c, delimiter=';')
        for i in reader:
                dict = {}
                dict['id'] = i[0]
                dict['title'] = i[1]
                dict['content'] = i[2]
                dict['create date'] = i[3]
                conclusion.append(dict)
    with open('note_directory.json', 'w', encoding='utf-8') as n_d:
        json.dump(conclusion, n_d, indent=2)
    print('Import is completed\n')