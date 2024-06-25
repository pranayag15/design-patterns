# https://youtu.be/u8DttUrXtEw?si=gBRROfjR4_ACIZFd

from .drive_strategy import DriveStrategy, NormalDrive, SpecialDrive


class Vehicle:
    def __init__(self, drive_strategy: DriveStrategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()


class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDrive())


class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDrive())


class Passenger(Vehicle):
    def __init__(self):
        super().__init__(NormalDrive())


passenger = Passenger()
passenger.drive()
