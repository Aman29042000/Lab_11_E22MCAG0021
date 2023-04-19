
##e22mcag0021
##aman choudhary

from Duck import Duck
from FlyWithWings import FlyWithWings
from MuteQuack import MuteQuack


class RedHeadDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a Red Headed duck")
