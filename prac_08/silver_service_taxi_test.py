
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():

    taxi = SilverServiceTaxi("Taxi", 18, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()

