# battery.py

class Battery:
    """A simple attempt to model battery for a car."""
    def __init__(self, last_service_date, current_date):
        """Initialize battery attributes."""
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_should_be_serviced(self):
        """Check if battery needs servicing."""
        pass

class SpindlerBattery(Battery):
    """A simple attempt to model a Spindler battery."""
    def __init__(self, last_service_date, current_date):
        """Initialize Spindler battery attributes."""
        super().__init__(last_service_date, current_date)

    def battery_should_be_serviced(self):
        """Check if Spindler battery needs servicing."""
        if self.current_date - self.last_service_date > 2:
            return True
        else:
            return False
        
class Nubbin(Battery):
    """A simple attempt to model a Nubbin battery."""
    def __init__(self, last_service_date, current_date):
        """Initialize Nubbin battery attributes."""
        super().__init__(last_service_date, current_date)

    def battery_should_be_serviced(self):
        """Check if Nubbin battery needs servicing."""
        if self.current_date - self.last_service_date > 4:
            return True
        else:
            return False
            
