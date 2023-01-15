from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):

    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare_number(self):
        return self.flag_fall + super().get_fare()


