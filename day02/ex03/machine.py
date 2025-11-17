from beverages import *

class CoffeeMachine:
    __init__(self):
        pass
    
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"
        
    class BrokenMachine(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def serve(self, beverage):
        