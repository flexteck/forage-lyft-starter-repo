class Engine:
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        """Initializing the engine class"""
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date

    def engine_should_be_serviced(self):
        """Check if engine needs servicing"""
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        """Initializing the Capulet engine class"""
        super().__init__(last_service_mileage, current_mileage, last_service_date)

    def engine_should_be_serviced(self):
        """Check if Capulet engine needs servicing"""
        if self.current_mileage - self.last_service_mileage > 30000:
            return True
        else:
            return False
        
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        """Initializing the Willoughby engine class"""
        super().__init__(last_service_mileage, current_mileage, last_service_date)

    def engine_should_be_serviced(self):
        """Check if Willoughby engine needs servicing"""
        if self.current_mileage - self.last_service_mileage > 60000:
            return True
        else:
            return False
        
class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        """Initializing the Sternman engine class"""
        super().__init__(0, 0, last_service_date)  # Assuming initial current_mileage is 0
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        """Check if Sternman engine needs servicing"""
        return self.warning_light_is_on
