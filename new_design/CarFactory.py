import Car
from CapuletEngine import CapuletEngine
from WilloughbyEngine import WilloughbyEngine
from SternmanEngine import SternmanEngine
from SpindlerBattery import SpindlerBattery
from NubbinBattery import NubbinBattery


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, current_mileage: int,
                          last_service_mileage: int) -> Car:
        engine = SternmanEngine()
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
