from new_design.Tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, _wear):
        self.wear = _wear

    def needs_service(self) -> bool:
        if sum(self.wear) >= 3:
            return True
        else:
            return False
