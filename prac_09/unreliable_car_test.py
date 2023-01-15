import random

from prac_09.unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("My car", 100, 40)
    if random.uniform(0, 100) < my_car.reliability:
        print(f"distance driven:{my_car.drive(random.randint(1, 100))}km")
    else:
        print(f"distance driven:{my_car.drive(0)}km")


main()
