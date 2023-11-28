from Engine.engine import Engine

class SternmanEngine(Engine):
    """Initializes the SternmanEngine class."""
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        """Determines if the SternmanEngine needs service."""
        return self.warning_light_is_on