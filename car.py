from abc import ABC, abstractmethod
from car_parts import engine,battery
from servicable import Servicable

class Car(Servicable):
    def __init__(self, engine: engine.Engine,battery: battery.Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
