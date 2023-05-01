# USE OF RANDOM IN PYTHON
import random
class Dice():

    def roll(self,a,b):
        first = random.randint(a, b)
        second = random.randint(a, b)

        return first,second



dice = Dice()

print(dice.roll(1,6))