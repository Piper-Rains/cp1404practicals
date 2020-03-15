MIN_LENGTH = 4


def main():

    password = get_password()

    asterisks_password(password)


def asterisks_password(password):
    print("Your password has been approved:")
    for i in range(len(password)):
        print("*", end=' ')
    print()


def get_password():
    print("Please enter a valid password, with a length no less than {}".format(MIN_LENGTH))
    password = input("> ")
    while len(password) < MIN_LENGTH:
        print("Invalid password length")
        print("Please enter a valid password, with a length no less than {}".format(MIN_LENGTH))
        password = input("> ")
    return password


main()

