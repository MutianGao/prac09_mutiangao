from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def get_valid_taxi(taxis):
    pass


def main():
    bill = 0.00
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    now_taxi = None
    print("Let's Drive!")
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != "q":

        if user_choice == "c":
            count = 0
            print("Taxis available:")
            for taxi in taxis:
                print('{} -- {}'.format(count, taxi))
                count = count + 1
            try:
                choose_taxi = int(input("Choose taxi: "))
                now_taxi = taxis[choose_taxi]
            except IndexError:
                print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")

        elif user_choice == "d":
            if now_taxi:
                drive_distance = int(input("Drive how far? "))
                now_taxi.drive(drive_distance)
                print(f"Your {now_taxi.name} trip cost you ${now_taxi.get_fare()}")
                bill += now_taxi.get_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${ bill}")
        print(MENU)
        user_choice = input(">>> ").lower()

    print(f"Total trip cost: ${ bill}")
    print("Taxis are now:")
    count = 0
    for taxi in taxis:
        print('{} -- {}'.format(count, taxi))
        count = count + 1


main()
