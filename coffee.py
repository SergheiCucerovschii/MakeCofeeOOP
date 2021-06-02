names = ("Espresso", "Cappuccino", "Robusta")

ingr1 = {"water": "100ml", "cofee": "15g", }
ingr2 = {"water": "100ml", "cofee": "10g", "milk": "75ml"}
ingr3 = {"water": "100ml", "cofee": "20g", "heavy cream": "50ml"}


class CoffeeMachine:
    def __init__(self, brand="Philips"):
        self.brand = brand

    def __str__(self):
        return f"The Cofee Machine is {self.brand}"

    def makeCoffee(self, name, ingredients):
        if name in names:
            return _CoffeeDrink(name, ingredients)
        else:
            raise TypeError(f"This machine can make only {names} types of Coffee")


class _CoffeeDrink:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"Your drink is {self.name}, contains of {self.ingredients}"
