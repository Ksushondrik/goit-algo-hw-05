import functions as fu


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = fu.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(fu.add_contact(args, contacts))
        elif command == "change":
            print(fu.change_contact(args, contacts))
        elif command == "phone":
            print(fu.show_phone(args, contacts))
        elif command == "all":
            print(fu.show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
