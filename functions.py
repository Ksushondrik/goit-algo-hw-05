import decor as de

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@de.input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@de.input_error
def change_contact (args, contacts):
    if args[0] in contacts.keys() :
        name, phone = args
        contacts[name] = phone
        return "Contact updated."
    else:
        raise Exception("Not found!")

@de.input_error
def show_phone (args, contacts):
    name = args[0]
    if name in contacts.keys() :
        return f"Pfone {name}: {contacts[name]}"
    else:
        raise Exception("Not found!")

@de.input_error
def show_all (contacts):
    if bool(contacts) :
        for key, value in contacts.items():
            print(f"{key:10}: {value:10}")
    else:
        raise Exception("No mach to show!")