from collections import UserDict


#create a limit for the length up to 50 symbols
class Title():

    def __init__(self, title):
        self.title = title

#create a limit for the length up to 300 symbols
class Body():
    
    def __init__(self, body):
        self.title = body

#Nikita
class Tag():
    pass

#create a note with title and body
class Note():
    
    def __init__(self, title: Title = None, body: Body = None):
        self.title = title
        self.body = body


#add note to notebook
class Notebook(UserDict):

    def add_record(self, note):
        self.data[note[0]] = note

def add_note():
    print('Note added!')

def search_note():
    print('Note searched!')

def change_note():
    print('Note edited!')

def delete_note():
    print('Note deleted!')

def exit_helper():
    print('Good bye!')

# #decorator
# def input_error(func):

#     def inner(*args):

#         try: 
#             func(*args)
#         except IndexError:
#             print('Your input should be in the following order: /{command/} /{Name/} /{Phone Number/}')
#             func(*args)
#         except KeyError:
#             print('Either the command or the name is wrong, please try again!')
#         except ValueError:
#             print('Please try again!')
#             func(*args)

            
#     return inner

COMMANDS = {
    'add': add_note,
    'search': search_note,
    #'show': show_notes,
    'edit': change_note,
    'delete': delete_note,
    'exit': exit_helper
    }

def handler(command_name):
    return COMMANDS[command_name]

#@input_error
def main():

    print(
        """
        You are in your notebook. Enter one of the following commands: \n
        add ...
        search ...
        edit ...
        delete ...
        exit 
        """
    )

    while True:

        user_input = input(">>> ") #add number
        input_parsed = user_input.split() #['add', 'number']
        command = input_parsed[0].lower() #add

        #handle exceptions
        if command not in COMMANDS.keys():
            print('Please enter one of the commands from the list!')
        else:
            handler(command)()

        if user_input == 'exit':
            exit_helper()
            break


if __name__ == '__main__':
    main()