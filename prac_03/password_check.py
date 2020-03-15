
MIN_LENGTH = 4

print("Please enter a valid password, with a length no less than {}".format(MIN_LENGTH))
password = input("> ")

while len(password) < MIN_LENGTH:
    print("Invalid password length")
    print("Please enter a valid password, with a length no less than {}".format(MIN_LENGTH))
    password = input("> ")

print("Your password has been approved:")
for i in range(len(password)):
    print("*", end=' ')
print()
