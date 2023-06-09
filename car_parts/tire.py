from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self,tire_array):
        self.tire_array = tire_array
    @abstractmethod
    def needs_service(self):
        pass
