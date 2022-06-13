import Battery


class NubbinBattery(Battery):
    def __init__(self, _last_service_date, _current_date):
        self.last_service_date = _last_service_date
        self.current_date = _current_date

    def needs_service(self) -> bool:
        if self.current_date - 4 >= self.last_service_date:
            return True
        else:
            return False