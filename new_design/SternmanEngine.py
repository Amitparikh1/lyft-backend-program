import Engine


class SternmanEngine(Engine):
    def __init__(self, _warning_light: bool = False):
        self.warning_light = _warning_light

    def needs_service(self) -> bool:
        return self.warning_light
