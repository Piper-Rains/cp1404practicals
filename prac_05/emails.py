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


def get_name_in_email(email):
    username = email.split('@')[0]
    parts = username.split('.')
    name = " ".join(parts).title()
    return name


main()
