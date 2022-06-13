from new_design.Battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, _last_service_date, _current_date):
        self.last_service_date = _last_service_date
        self.current_date = _current_date

    def needs_service(self) -> bool:
        service_by = self.last_service_date.replace(self.last_service_date.year + 3)
        if self.current_date >= service_by:
            return True
        else:
            return False
