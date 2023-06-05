from abc import ABC, abstractmethod
from car_parts import engine,battery

class Car():
    def __init__(self, engine: engine.Engine,battery: battery.Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
