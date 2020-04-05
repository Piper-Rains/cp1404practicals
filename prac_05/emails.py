def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = get_name_in_email(email)
        check_name = input("Is your name {}? (Y/N) ".format(name))
        if check_name.upper() != "Y" and check_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{0} ({1})".format(name, email))


def get_name_in_email(email):
    username = email.split('@')[0]
    parts = username.split('.')
    name = " ".join(parts).title()
    return name


main()
