from Engine.capulet_engine import CapuletEngine
from Engine.sternman_engine import SternmanEngine
from Engine.willoughby_engine import WilloughbyEngine
from Battery.nubbin_battery import NubbinBattery
from Battery.spindler_battery import SpindlerBattery

from car import Car


class CarFactory(Car):
    """ creates cars """

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        """ creates a Calliope car """
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)