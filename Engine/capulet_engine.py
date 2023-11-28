from Engine.engine import Engine

class CapuletEngine(Engine):
    """Initializes the CapuletEngine class."""
    def __init(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        """Determines if the CapuletEngine needs service."""
        if self.current_mileage - self.last_service_mileage >= 3000:
            return True
        else:
            return False