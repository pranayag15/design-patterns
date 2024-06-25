from abc import ABC, abstractmethod


class BasePizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass


class MargheritaPizza(BasePizza):
    def get_cost(self):
        return 100


class VegDelightPizza(BasePizza):
    def get_cost(self):
        return 150
