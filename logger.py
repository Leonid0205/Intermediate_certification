from datetime import datetime as dt

def create_note_log(list):
    time = dt.now().strftime('%Y-%M-%D %H:%M:%S')
    with open ('log.txt', 'a') as log:
        log.write('New Note created: {} {} \n'
                  .format(list, time))
def delete_note_log(list):
    time = dt.now().strftime('%Y-%M-%D %H:%M:%S')
    with open ('log.txt', 'a') as log:
        log.write('Note was deleteed: {} {}\n'
                  .format(list, time))
def change_note_log(list):
    time = dt.now().strftime('%Y-%M-%D %H:%M:%S')
    with open ('log.txt', 'a') as log:
        log.write('Note was changed: {} {}\n'
                  .format(list, time))
def import_log():
    time = dt.now().strftime('%Y-%M-%D %H:%M:%S')
    with open ('log.txt', 'a') as log:
        log.write('Import all notes: {}\n'
                  .format(time))
def export_log():
    time = dt.now().strftime('%Y-%M-%D %H:%M:%S')
    with open ('log.txt', 'a') as log:
        log.write('Export all notes: {}\n'
                  .format(time))