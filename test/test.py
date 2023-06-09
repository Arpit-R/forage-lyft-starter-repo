import unittest
from datetime import datetime
import unittest
from car_parts.engine_type import *
from car_parts.battery_type import *

class TestEngine(unittest.TestCase):
    def testCapuletEngineNeedsService(self):
        engine = CapuletEngine(4000,120)
        self.assertTrue(engine.needs_service())

    def testCapuletEngineNotNeedsService(self):
        engine = CapuletEngine(4000,3500)
        self.assertTrue(engine.needs_service())
    
    def testSternmanEngineNeedsService(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def testSternmanEngineNotNeedsService(self):
        engine = SternmanEngine(False)
        self.assertTrue(engine.needs_service())
    
    def testWilloughbyEngineNeedsService(self):
        engine = WilloughbyEngine(9000,1000)
        self.assertTrue(engine.needs_service())
    
    def testWilloughbyEngineNotNeedsService(self):
        engine = WilloughbyEngine(5000,4000)
        self.assertTrue(engine.needs_service())
        
    
class TestBattery(unittest.TestCase):
    def testNubbinBatteryNeedsService(self):
        battery = NubbinBattery(datetime(2015,1,1))
        self.assertTrue(battery.needs_service())
    
    def testNubbinBatteryNotNeedsService(self):
        battery = NubbinBattery(datetime(2023,1,1))
        self.assertTrue(battery.needs_service())
    
    def testSpindlerBatteryNeedsService(self):
        battery = SpindlerBattery(datetime(2020,1,1))
        self.assertTrue(battery.needs_service())
    
    def testSpindlerBatteryNotNeedsService(self):
        battery = SpindlerBattery(datetime(2023,1,1))
        self.assertTrue(battery.needs_service())
    
    

if __name__ == '__main__':
    unittest.main()
