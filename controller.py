import view
import change_contact
import checks
import create
import delete
import export
import import_j
import logger
import search
import reception


def button_click():
    while True:
        reception.reception()
        press = checks.check(8)
        if press == 1:
            note_dir = view.get_value()
            create.create_note_directory(note_dir)
            logger.create_note_log(note_dir)
        elif press == 2:
            if checks.check_empty_dir():
                reception.search_option()
                search_press = checks.check(3)
                result = search.search_note(search_press)
                if len(result) != 0:
                    view.show_note(result)
                else:
                    print('Sorry there is no such note')
                if len(result) == 1:
                    press_action = reception.action()
                    if press_action == 1:
                        change_contact.note_change(result)
                        logger.change_note_log(result[0])
                    if press_action == 2:
                        delete.delete_note(result)
                        logger.delete_note_log(result[0])
                    if press_action == 3:
                        continue
                    if press_action == 4:
                        exit()
            else:
                continue
        elif press == 3:
            if checks.check_empty_dir():
                reception.change_option()
                search_press = checks.check(3)
                result = search.search_note(search_press)
                if len(result) != 0:
                    view.show_note(result)
                    change_contact.note_change(result)
                    logger.change_note_log(result[0])
                else:
                    print('Sorry there is no such note')   
        elif press == 4:
            if checks.check_empty_dir():
                reception.del_option()
                search_press = checks.check(3)
                result = search.search_note(search_press)
                if len(result) != 0:
                    view.show_note(result)
                    delete.delete_note(result)
                    logger.change_note_log(result[0])
                else:
                    print('Sorry there is no such note')   
        elif press == 5:
            if checks.check_empty_dir():
                view.show_note_dir()
        elif press == 6:
            import_j.import_dir()
            logger.import_log()
        elif press == 7:
            export.export()
            logger.export_log()
        else: 
            break