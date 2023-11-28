
from abc import ABC, abstractmethod
from model import Engine, Battery

class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass

class MyCar(Car, ABC):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)

    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()
