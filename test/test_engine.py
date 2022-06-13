import unittest

from new_design.CapuletEngine import CapuletEngine
from new_design.WilloughbyEngine import WilloughbyEngine
from new_design.SternmanEngine import SternmanEngine


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        curr = 40000
        last = 0
        engine = CapuletEngine(last, curr)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        curr = 20000
        last = 0
        engine = CapuletEngine(last, curr)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        curr = 70000
        last = 0
        engine = WilloughbyEngine(last, curr)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        curr = 40000
        last = 0
        capulet_engine = WilloughbyEngine(last, curr)
        self.assertFalse(capulet_engine.needs_service())


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning = True
        engine = SternmanEngine(warning)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning = False
        engine = SternmanEngine(warning)
        self.assertTrue(engine.needs_service())
