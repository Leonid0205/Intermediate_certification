import json

def check(n):
    while True:
        try:
            item = int(input('Input an item of a menu: '))
            if 0 < item <= n:
                break
            else: 
                print('There is no such item in the menu')
                continue
        except:
            print('Incorrect value was inputed')
    return item
def check_empty_dir():
    try:
        with open('note_directory.json', 'r', encoding='utf-8') as n_d:
            note_dir = json.load(n_d)
            return True
    except:
        print('\nNotes directory is empty')
        return False
def check_length_title(str):
    while True:
        try:
            result = input(f'Input {str} (length of {str} needs to be less than 20 symbols): ')
            if len(result) < 20:
                break
            else:
                print(f'{str} length needs to be less than 20 symbols')
        except:
            print('Incorrect value was inputed')
    return result

def check_length_content(str):
    while True:
        try:
            result = input(f'Input {str} (length of {str} needs to be less than 50 symbols): ')
            if len(result) < 50:
                break
            else:
                print(f'{str} length needs to be less than 50 symbols')
        except:
            print('Incorrect value was inputed')
    return result

def check_id():
    while True:
        try:
            id = int(input('Input an id: '))
            return id
        except:
            print('Incorrect value was inputed')