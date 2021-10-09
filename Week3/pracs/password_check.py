MINIMUM_LENGTH = 4

def main():
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)


def get_password(MINIMUM_LENGTH):
    password = input("Enter password of length at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short")
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    return password


def print_stars(password_length):
    print('*' * len(password_length))


main()
