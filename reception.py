from checks import check

def reception():
    print('\nHello')
    print('\nYou can:\n'
          '1 - Create a note\n'
          '2 - Find a note\n'
          '3 - Change a note\n'     
          '4 - Delete a note\n'
          '5 - Show all notes\n'
          '6 - Import of notes\n'
          '7 - Export of notes\n'
          '8 - Exit')
def search_option():
    print('Search by:\n'
          '1 - id\n'
          '2 - Title\n'
          '3 - Contetnt')
def change_option():
    print('In order to change the note you need to choose one by:\n'
          '1 - id\n'
          '2 - Title\n'
          '3 - Contetnt')
def action():
    print('What you want to do with contact:\n'
          '1 - Change\n'
          '2 - Delete\n'
          '3 - Exit to the main menu\n'
          '4 - Exit the program')
    return check(4)
def del_option():
      print('In order to delete the note you need to choose one by:\n'
          '1 - id\n'
          '2 - Title\n'
          '3 - Contetnt')