from tire import Tire



class CarriganTire(Tire):
    def __init__(self, tire_array):
        super().__init__(tire_array)
    
    def needs_service(self):
        return any(worn_value >= 0.9 for worn_value in self.tire_array)
    
class OctoprimeTire(Tire):
    def __init__(self, tire_array):
        super().__init__(tire_array)
    
    def needs_service(self):
        return sum(self.tire_array) >= 3
