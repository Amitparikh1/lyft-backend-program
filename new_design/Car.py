from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, _engine, _battery, _tires):
        self.engine = _engine
        self.battery = _battery
        self.tires = _tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
