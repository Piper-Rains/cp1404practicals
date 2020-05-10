
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():

    total_bill = 0
    current_taxi = ""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    menu_selection = input(">>> ").lower()

    while menu_selection != "q":
        if menu_selection == "c":
            print("Taxis Available: ")
            list_available_taxis(taxis)
            taxi_choice = receive_taxi_choice(taxis)
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(total_bill))
            print(MENU)
            menu_selection = input(">>> ").lower()
        elif menu_selection == "d":
            if current_taxi != "":
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
                total_bill += trip_cost
                print("Bill to date: ${:.2f}".format(total_bill))
                print(MENU)
                menu_selection = input(">>> ").lower()
            else:
                print("Please choose a taxi from the list before driving.")
        else:
            print("Invalid menu input")
            print("Bill to date: ${:.2f}".format(total_bill))
            print(MENU)
            menu_selection = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    list_available_taxis(taxis)


def list_available_taxis(taxis):
    """ Display numbered list of taxis """
    taxi_number = 0
    for taxi in taxis:
        print("{} - {}".format(taxi_number, taxi))
        taxi_number += 1


def receive_taxi_choice(taxis):
    """ Receive taxi choice with error checking """
    while True:
        try:
            taxi_choice = int(input("Choose taxi: "))
            while True:
                while taxi_choice < 0 or taxi_choice > (len(taxis) - 1):
                    if taxi_choice < 0:
                        print("Taxi choice number must be >= 0")
                        taxi_choice = int(input("Choose taxi: "))
                    else:
                        print("Invalid taxi choice")
                        taxi_choice = int(input("Choose taxi: "))
                else:
                    break
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            break
    return taxi_choice


main()
