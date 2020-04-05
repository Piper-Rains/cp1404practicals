def main():
    email_to_name = {}
    email = input("Email: ")


def get_name_in_email(email):
    username = email.split('@')[0]
    parts = username.split('.')
    name = " ".join(parts).title()
    return name


main()
