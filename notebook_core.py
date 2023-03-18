from collections import UserDict


class Title:

    def __init__(self):
        self.__title = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_value):
        if len(new_value) <= 50:
            self.__title = new_value.capitalize()
        else:
            print('>>> Your title is longer than 50 symbols. Please, make it shorter!')



class Body():
    
    def __init__(self):
        self.__body = None

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_value):
        if len(new_value) <= 300:
            self.__body = new_value
        else:
            print('>>> Your note is longer than 300 symbols. Please, make it shorter!')



class Note():
    
    def __init__(self):
        self.__note = None

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, new_list):
        self.__note = new_list



class Notebook(UserDict):

    #key: Title, value: Body -> change to Note later on
    def add(self, note):
        self.data[note.note[0]] = note.note[1]
        print('>>> Note added!')


def input_error(func):

    def inner(*args):

        try: 
            func(*args)
        except IndexError:
            print('Index Error! Please try again!')
            func(*args)
        except KeyError:
            print('Key Error! Please try again!')
            func(*args)
        except ValueError:
            print('Value Error! Please try again!')
            func(*args)
            
    return inner


    
@input_error
def add_note(user_input):
    
    title = user_input.removeprefix('add').strip().capitalize()
    new_title = Title()
    new_body = Body()
    new_note = Note()

    body_input = input(f'Enter content for new note \'{title}\' >>> ')

    new_title.title = title
    new_body.body = body_input
    new_note.note = [new_title.title, new_body.body]

    default_notebook.add(new_note)


@input_error
def search_note(user_input):

    title = user_input.removeprefix('search').strip()
    result = '>>> Note not found! Try again!'

    for key in default_notebook.data.keys():
        if title.capitalize() == key:
            result = f'>>> The following note found: \n {key} : {default_notebook.data[key]}'

    print(result)
    

@input_error
def show_all(user_input):

    print(f'>>> This is your notebook: \n {default_notebook}')


@input_error
def edit_note(user_input):

    new_note = Body()
    title = user_input.removeprefix('edit').strip().capitalize()

    if title not in default_notebook.data.keys():
        print('>>> Note with this name does not exist! Try again!')
    else:
        new_value = input(f'Enter new content for \'{title}\'>>> ')
        new_note.body = new_value
        default_notebook.data[title] = new_note.body
        print('>>> Note edited!')


@input_error
def delete_note(user_input):

    title = user_input.removeprefix('delete').strip().capitalize()

    if title not in default_notebook.data.keys():
        print('>>> Note with this name does not exist! Try again!')
    else:
        default_notebook.data.pop(title)
        print('>>> Note deleted!')


@input_error
def help(user_input):

    print(
        """
        You can type one of the following commands: \n
        add [new title] - to add a new note 
        search [title] - to find one of your notes
        show - to see all current notes
        edit [title] - to change a note content
        delete [title] - to erase a note 
        help - to see the list of commands
        exit - to end session
        """
    )


@input_error
def exit_helper():

    print('>>> Good bye!')


COMMANDS = {
    'add': add_note,
    'search': search_note,
    'show': show_all,
    'edit': edit_note,
    'delete': delete_note,
    'help' : help,
    'exit': exit_helper
    }


def handler(command_name):
    return COMMANDS[command_name]


def main():

    print(
        """
        You are in your notebook. Enter one of the following commands: \n
        add [new title]
        search [title]
        show
        edit [title]
        delete [title]
        help
        exit 
        """
    )

    while True:

        user_input = input(">>> ")
        input_parsed = user_input.split()
        command = input_parsed[0].lower()

        if command not in COMMANDS.keys():
            print('Please enter one of the commands from the list!')
        elif command == 'exit':
            exit_helper()
            break
        else:
            handler(command)(user_input)


default_notebook = Notebook()


if __name__ == '__main__':
    main()