import json
import csv

def export():
    with open('note_directory.json', 'r', encoding='utf-8') as n_d:
        tel_dir = json.load(n_d)
    with open('note_directory.csv', 'w', encoding='utf-8') as n_d_c:
        writer = csv.writer(n_d_c, delimiter=';', lineterminator='\r')
        writer.writerow(['id', 'title', 'content', 'create date'])
        for i in tel_dir:
            writer.writerow([i['id'], i['title'], i['content'], i['create date']])
    print('Export is completed\n')