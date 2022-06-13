
class Car:
    def __init__(self, _engine, _battery):
        self.engine = _engine
        self.battery = _battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()