from abc import ABC, abstractmethod


class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass


class NormalDrive(DriveStrategy):
    def drive(self):
        print("Normal Drive")


class SpecialDrive(DriveStrategy):
    def drive(self):
        print("Special Drive")
