import unittest
from datetime import datetime

from new_design.SpindlerBattery import SpindlerBattery
from new_design.NubbinBattery import NubbinBattery


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        curr = datetime(2022, 6, 12)
        last = datetime(2019, 1, 1)
        battery = SpindlerBattery(last, curr)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        curr = datetime(2022, 6, 12)
        last = datetime(2020, 6, 12)
        battery = SpindlerBattery(last, curr)
        self.assertFalse(battery.needs_service())


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        curr = datetime(2022, 6, 12)
        last = datetime(2016, 1, 1)
        battery = NubbinBattery(last, curr)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        curr = datetime(2022, 6, 12)
        last = datetime(2021, 6, 12)
        battery = NubbinBattery(last, curr)
        self.assertFalse(battery.needs_service())
