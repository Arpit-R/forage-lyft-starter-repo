from datetime import datetime
from car import Car
#from car_parts import engine_type,battery_type
from car_parts.engine_type import *
from car_parts.battery_type import *

class CarFactory():
    @staticmethod
    def CreateCalliope(last_service_date, current_milage, last_service_milage):
        return Car(CapuletEngine(current_milage,last_service_milage),SpindlerBattery(last_service_date))
    
    @staticmethod
    def CreateGlissade(last_service_date, current_milage, last_service_milage):
        return Car(WilloughbyEngine(current_milage,last_service_milage),SpindlerBattery(last_service_date))
    
    @staticmethod
    def CreatePalindrome(last_service_date, warning_light_is_on):
        return Car(SternmanEngine(warning_light_is_on),SpindlerBattery(last_service_date))
    
    @staticmethod
    def CreateRorschach(last_service_date, current_milage, last_service_milage):
        return Car(WilloughbyEngine(current_milage,last_service_milage),NubbinBattery(last_service_date))
    
    @staticmethod
    def CreateThovex(last_service_date, current_milage, last_service_milage):
        return Car(CapuletEngine(current_milage,last_service_milage),NubbinBattery(last_service_date))