from collections import UserDict
from copy import copy
import json
from os.path import isfile


file_name = "Contacts.json"
path = "./Contacts.json"

# create a limit for the length up to 50 symbols
class Title:
    def __init__(self):
        self.title = None


# create a limit for the length up to 300 symbols
class Body:
    def __init__(self):
        self.body = None


# Nikita
class Tag:
    def __init__(self) -> None:
        self.__tag = None

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value: str):
        tag_list = value.split(" ")
        self.__tag = tag_list


# create a note with title and body
class Note:
    def __init__(self) -> None:
        self.__note_components = list

    @property
    def note_components(self):
        return self.__note_components

    @note_components.setter
    def note_components(self, note_value):
        self.__note_components = note_value


# add note to notebook
class Notebook(UserDict):
    def add_record(self, note):
        self.data[note.note_components[0]] = note


def add_note():
    print("Note added!")


def search_note():
    print("Note searched!")


def change_note():
    print("Note edited!")


def delete_note():
    print("Note deleted!")


def find_by_tag(*args):
    tags = args[0]
    result_tags = Notebook()
    buff_note = Note()
    for i in tags:
        for val in notebook.data.values():
            if val.note_components[2].tag:
                if i in val.note_components[2].tag:
                    buff_note.note_components = val.note_components
                    result_tags.add_record(copy(buff_note))
    sort_by_alphabet(result_tags)


def sort_by_alphabet(notes: Notebook):
    title_list = []
    sorted_notes = Notebook()
    for i in notes.data.values():
        title_list.append(copy(i.note_components[0].title.split()))
    for j in title_list:
        title_string = " ".join(j)
        for val in notebook.data.values():
            if title_string in val.note_components[0].title:
                sorted_notes.add_record(val)
    tag_display(sorted_notes)


def tag_display(result_tags):
    for val in result_tags.data.values():
        print(f"Title: {val.note_components[0].title}")
        print(f"Body: {val.note_components[1].body}")
        print(f"Tags: {val.note_components[2].tag}\n")


def save(notebook):
    result = {}
    with open(file_name, "w") as fh:
        for key, val in notebook.data.items():
            notes_list = []
            note = {}
            note["Title"] = val.note_components[0].title
            note["Body"] = val.note_components[1].body
            if val.note_components[2]:
                note["Tags"] = val.note_components[2].tag
            notes_list.append(note)
            result[key.title] = notes_list
        json.dump(result, fh, indent=4)


def restore():
    global notebook
    with open(file_name, "r") as fh:
        unpacked = json.load(fh)
        for val in unpacked.values():
            tags = Tag()
            title = Title()
            body = Body()
            note = Note()
            title.title = val[0]["Title"]
            body.body = val[0]["Body"]
            if "Tags" in val[0].keys():
                tags.tag = " ".join(val[0]["Tags"])
            note.note_components = [title, body, tags]
            notebook.data[title] = copy(note)


def exit_helper(*args):
    print("Good bye!")


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
    "add": add_note,
    "search": search_note,
    #'show': show_notes,
    "edit": change_note,
    "delete": delete_note,
    "find": find_by_tag,
    "exit": exit_helper,
}


def handler(command_name):
    return COMMANDS[command_name]


title_1 = Title()
title_1.title = "First title about fish"
body_1 = Body()
body_1.body = "First body"
tag_1 = Tag()
tag_1.tag = "fish sea ocean whale dolphin"
note_1 = Note()
note_1.note_components = [title_1, body_1, tag_1]
title_2 = Title()
title_2.title = "Second title about sport and mood"
body_2 = Body()
body_2.body = "Second body"
tag_2 = Tag()
tag_2.tag = "sport football basketball tennis train"
note_2 = Note()
note_2.note_components = [title_2, body_2, tag_2]
title_3 = Title()
title_3.title = "Third title about football"
body_3 = Body()
body_3.body = "Third body"
tag_3 = Tag()
tag_3.tag = "football ball red_card yellow_card"
note_3 = Note()
note_3.note_components = [title_3, body_3, tag_3]
notebook = Notebook()
title_4 = Title()
title_4.title = "Third title about footbbll"
body_4 = Body()
body_4.body = "Third body"
tag_4 = Tag()
tag_4.tag = "football ball red_card yellow_card"
note_4 = Note()
note_4.note_components = [title_4, body_4, tag_4]
notebook = Notebook()
notebook.add_record(note_1)
notebook.add_record(note_2)
notebook.add_record(note_3)
notebook.add_record(note_4)
# @input_error
def main():

    print(
        """
        You are in your notebook. Enter one of the following commands: \n
        add ...
        search ...
        edit ...
        delete ...
        find ...
        exit 
        """
    )

    while True:
        if isfile(path):
            restore()
        user_input = input(">>> ")  # add number
        input_parsed = user_input.split()  # ['add', 'number']
        command = input_parsed[0].lower()  # add

        # handle exceptions
        if command not in COMMANDS.keys():
            print("Please enter one of the commands from the list!")
        else:
            handler(command)(input_parsed[1:])

        if user_input == "exit":
            exit_helper()
            break
    tag_display(notebook)
    save(notebook)


if __name__ == "__main__":
    main()
