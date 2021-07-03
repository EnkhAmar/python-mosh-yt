from random import randint

class Dice:
    def roll(self):
        result = (randint(1, 6), randint(1, 6))
        return result

    def throw(self):
        first = randint(1, 6)
        second = randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
print(dice.throw())