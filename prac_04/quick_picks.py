
import random

NUMBERS_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quickpicks = int(input("How many quick picks?: "))

    while number_of_quickpicks < 0:
        print("Your number of quick picks must be greater than zero")
        number_of_quickpicks = int(input("How many quick picks?: "))

    for i in range(number_of_quickpicks):
        quickpick = []

        for k in range(NUMBERS_IN_LINE):
            number = random.randint(MINIMUM, MAXIMUM)

            while number in quickpick:
                number = random.randint(MINIMUM, MAXIMUM)
            quickpick.append(number)

        quickpick.sort()
        print(*quickpick)


main()