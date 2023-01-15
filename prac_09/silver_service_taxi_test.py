from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    hummer_car = SilverServiceTaxi('Hummer', 200, 4)
    print(hummer_car)
    Text_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    Text_taxi.drive(18)
    print(Text_taxi)
    print("Fare:", Text_taxi.get_fare_number(), "$")


main()
