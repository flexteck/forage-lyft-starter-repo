from Battery.battery import Battery
from helper import calculate_service_date

class NubbinBattery(Battery):
    """Initializes NubbinBattery """
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        """checks if battery needs service"""
        date_for_ba3_service = calculate_service_date(self.last_service_date, 4)
        if date_for_ba3_service < self.current_date:
            return True
        else:
            return False