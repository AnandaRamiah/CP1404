def main():
    email_and_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        name_valid = input("Is your name {}? (Y/n) ".format(name))
        if name_valid.upper() != "Y" and name_valid != "":
            name = input("Name: ")
        email_and_name[email] = name
        email = input("Email: ")

    for email, name in email_and_name.items():
        print("{} ({})".format(name, email))


def extract_name(email):
    name = email.split('@')[0]
    parts = name.split('.')
    full_name = " ".join(parts).title()
    return full_name


main()