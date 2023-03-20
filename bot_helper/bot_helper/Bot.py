from bot_helper.address_book import *
from bot_helper.main import *
from bot_helper.notebook_final import *


def main():
    print(
        """This bot has 3 functions:
    Address book, Notebook and File sorter
    Please Enter one of this command:
    1) Address book
    2) Notebook
    3) File sorter
    or 'exit' to exit :)
    """
    )
    while True:
        command = input(">>> ").split(" ")
        if command[0].lower() == "address":
            main_address_book()
        elif command[0].lower() == "notebook":
            main_notebook()
        elif command[0].lower() == "file":
            path_function()
        elif command[0].lower() == "exit":
            break
        else:
            print("Such command does not exist. Try again ")
