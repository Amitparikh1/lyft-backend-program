import Engine


class CapuletEngine(Engine):
    def __init__(self, _last_service_miles=0, _current_mileage=0):
        self.last_service_miles = _last_service_miles
        self.current_mileage = _current_mileage

    def needs_service(self) -> bool:
        if self.current_mileage >= self.last_service_miles + 30000:
            return True
        else:
            return False
