from Engine.engine import Engine

class WilloughbyEngine(Engine):
    """Initializes the WilloughbyEngine class."""
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        """Determines if the WilloughbyEngine needs service."""
        if self.current_mileage - self.last_service_mileage >= 60000:
            return True
        else:
            return False