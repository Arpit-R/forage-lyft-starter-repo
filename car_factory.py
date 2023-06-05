from datetime import datetime
import car
from car_parts import engine_type,battery_type

class CarFactory():
    @staticmethod
    def CreateCalliope(last_service_date, current_milage, last_service_milage):
        return car.Car(engine_type.CapuletEngine(current_milage,last_service_milage),battery_type.SpindlerBattery(last_service_date))
    
    @staticmethod
    def CreateGlissade(last_service_date, current_milage, last_service_milage):
        return car.Car(engine_type.WilloughbyEngine(current_milage,last_service_milage),battery_type.SpindlerBattery(last_service_date))
    
    @staticmethod
    def CreatePalindrome(last_service_date, warning_light_is_on):
        return car.Car(engine_type.SternmanEngine(warning_light_is_on),battery_type.SpindlerBattery(last_service_date))
    
    @staticmethod
    def CreateRorschach(last_service_date, current_milage, last_service_milage):
        return car.Car(engine_type.WilloughbyEngine(current_milage,last_service_milage),battery_type.NubbinBattery(last_service_date))
    
    @staticmethod
    def CreateThovex(last_service_date, current_milage, last_service_milage):
        return car.Car(engine_type.CapuletEngine(current_milage,last_service_milage),battery_type.NubbinBattery(last_service_date))