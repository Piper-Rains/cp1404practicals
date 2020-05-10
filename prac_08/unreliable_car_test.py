from prac_08.unreliable_car import UnreliableCar


def main():

    car = UnreliableCar("Car", 100, 50)

    for i in range(1, 11):
        print("Attempting to drive {}km:".format(i))
        print("{} drove {}km".format(car.name, car.drive(i)))

    print(car)


main()
