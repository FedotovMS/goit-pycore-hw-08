import pickle

from commands import (
    add_contact,
    change_contact,
    show_phone,
    add_birthday,
    show_birthday,
    birthdays,
)
from models import AddressBook
from utils import parse_input

def save_data(book, filename="addressbook.pkl"):
    """Серіалізація AddressBook у файл."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    """Десеріалізація AddressBook із файлу."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))
            save_data(book)

        elif command == "change":
            print(change_contact(args, book))
            save_data(book)

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            for record in book.data.values():
                print(record)

        elif command == "add-birthday":
            print(add_birthday(args, book))
            save_data(book)

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()