from .drive_strategy import DriveStrategy, NormalDrive, SpecialDrive


class Vehicle:
    def drive(self):
        # All vehicle will have same drive or if overwrtie then code duplication
        print("Vehicle is driving")


class SportsVehicle(Vehicle):
    def drive(self):
        # code duplication
        return print("Special Vehicle is driving")


class OffRoadVehicle(Vehicle):
    def drive(self):
        # code duplication
        return print("Special Vehicle is driving")


class Passenger(Vehicle):
    def __init__(self):
        pass


passenger = Passenger()
passenger.drive()

sports = SportsVehicle()
sports.drive()
