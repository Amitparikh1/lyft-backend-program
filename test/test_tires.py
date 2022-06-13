import unittest
from datetime import datetime

from new_design.CarriganTires import CarriganTires
from new_design.OctoprimeTires import OctoprimeTires


class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        wear = [.9, .95, .7, .6]
        tires = CarriganTires(wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        wear = [.8, .85, .7, .6]
        tires = CarriganTires(wear)
        self.assertFalse(tires.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        wear = [.9, .95, .7, .6]
        tires = CarriganTires(wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        wear = [.1, .2, .3, .4]
        tires = CarriganTires(wear)
        self.assertFalse(tires.needs_service())