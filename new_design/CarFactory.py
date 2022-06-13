from Car import Car
from CapuletEngine import CapuletEngine
from WilloughbyEngine import WilloughbyEngine
from SternmanEngine import SternmanEngine
from SpindlerBattery import SpindlerBattery
from NubbinBattery import NubbinBattery
from CarriganTires import CarriganTires
from OctoprimeTires import OctoprimeTires



class CarFactory:
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int, wear) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int, wear) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on: bool, wear) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int, wear) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int, wear) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(wear)
        return Car(engine, battery, tires)
