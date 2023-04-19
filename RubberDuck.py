
##e22mcag0021
##aman choudhary


from Duck import Duck
from FlyNoWay import FlyNoWay
from Squeak import Squeak


class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm a RUBBER DUCK")
