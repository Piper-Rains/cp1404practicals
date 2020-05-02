from prac_06.guitar import Guitar


def main():
    """Program using the Guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print("{} ({}) : ${:.2f} added.".format(new_guitar.name, new_guitar.year, new_guitar.cost))
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    guitar_number = 1
    for guitar in guitars:
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(guitar_number, guitar.name, guitar.year,
                                                                   guitar.cost, vintage_string))
        guitar_number += 1


main()
