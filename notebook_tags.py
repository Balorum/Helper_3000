from collections import UserDict


class Title:
    def __init__(self) -> None:
        self.__title = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        upper_case = value[0].upper() + value[1:]
        if len(upper_case) > 50:
            print("Title is too long")
        else:
            self.__title = upper_case


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


class Body:
    def __init__(self) -> None:
        self.__body = None

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value: str):
        self.__body = value


class Note:
    def __init__(self) -> None:
        self.__note_components = list

    @property
    def note_components(self):
        return self.__note_components

    @note_components.setter
    def note_components(self, note_value):
        self.__note_components = note_value


class Notebook(UserDict):
    def add_record(self, note):
        self.data[note.note_components[0]] = note


"""a = Title()
b = Body()
c = Tag()
note = Note()
n_b = Notebook()
while not a.title:
    a.title = input("Enter the title: ")
while not b.body:
    b.body = input("Enter the body: ")
while not c.tag:
    c.tag = input("Enter the tag: ")
note.note_components = [a, b, c]
n_b.add_record(note)

print(n_b.data[a].note_components)

print(a.title)"""


def find_by_tag(tags, notebook):
    result_tags = Notebook()
    buff_note = Note()
    for i in tags:
        for val in notebook.data.values():
            if val.note_components[2].tag:
                if i in val.note_components[2].tag:
                    buff_note.note_components = val.note_components
                    result_tags.add_record(buff_note)
    tag_display(result_tags)


def tag_display(result_tags):
    for val in result_tags.data.values():
        print(f"Title: {val.note_components[0].title}")
        print(f"Body: {val.note_components[1].body}")
        print(f"Tags: {val.note_components[2].tag}\n")


title_1 = Title()
title_1.title = "First title about fish"
body_1 = Body()
body_1.body = "First body"
tag_1 = Tag()
tag_1.tag = "fish sea ocean whale dolphin"
note_1 = Note()
note_1.note_components = [title_1, body_1, tag_1]
title_2 = Title()
title_2.title = "Second title about sport"
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
notebook.add_record(note_1)
notebook.add_record(note_2)
notebook.add_record(note_3)

for key, val in notebook.data.items():
    print(f"{key.title}: {val.note_components}")

to_find = input("What tag or tags do you find? ").split(" ")
find_by_tag(to_find, notebook)
