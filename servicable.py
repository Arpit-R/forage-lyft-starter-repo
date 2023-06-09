from abc import ABC,abstractmethod

from car_parts.engine_type import *

class Servicable(ABC):
    @abstractmethod
    def needs_service(self):
        pass