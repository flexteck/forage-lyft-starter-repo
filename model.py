# model.py

from datetime import date
from car import *
from engine import *
from battery import *
from engine import CapuletEngine
from engine import WilloughbyEngine
from engine import sternman_engine

def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    engine = CapuletEngine(last_service_mileage, current_mileage, last_service_date)
    battery = Nubbin(last_service_date, current_date)
    return MyCar(engine, battery)

def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    engine = WilloughbyEngine(last_service_mileage, current_mileage, last_service_date)
    battery = SpindlerBattery(last_service_date, current_date)
    return MyCar(engine, battery)

def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
    engine = sternman_engine(last_service_date, warning_light_on)
    battery = Nubbin(last_service_date, current_date)
    return MyCar(engine, battery)

def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    engine = CapuletEngine(last_service_mileage, current_mileage, last_service_date)
    battery = Nubbin(last_service_date, current_date)
    return MyCar(engine, battery)

def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    engine = WilloughbyEngine(last_service_mileage, current_mileage, last_service_date)
    battery = SpindlerBattery(last_service_date, current_date)
    return MyCar(engine, battery)
