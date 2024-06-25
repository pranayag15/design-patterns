from .base_pizza import BasePizza


class ToppingsDecorator(BasePizza):
    # Inheriting BasePizza completes "is a" relationship and child class having BasePizza object completes "has a" relationship
    pass


class CheeseTopping(ToppingsDecorator):
    def __init__(self, pizza: BasePizza):
        self.pizza: BasePizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 10


class TomatoTopping(ToppingsDecorator):
    def __init__(self, pizza: BasePizza):
        self.pizza: BasePizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 20
