from new_design.Tires import Tires


class CarriganTires(Tires):
    def __init__(self, _wear):
        self.wear = _wear

    def needs_service(self) -> bool:
        for tire_wear in self.wear:
            if tire_wear >= .9:
                return True
        return False
