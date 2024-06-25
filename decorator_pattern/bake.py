# https://youtu.be/w6a9MXUwcfY?si=nTHJCDpm8mW-Nbg9

from .base_pizza import BasePizza, MargheritaPizza, VegDelightPizza
from .toppings import CheeseTopping, TomatoTopping

pizza1: BasePizza = TomatoTopping(CheeseTopping(MargheritaPizza()))
pizza2: BasePizza = TomatoTopping(CheeseTopping(VegDelightPizza()))

print("Complete MargheritaPizza Cost: ", pizza1.get_cost())
print("Complete VegDelightPizza Cost: ", pizza2.get_cost())
