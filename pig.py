import random


class Game:
    def __init__(self, dice, player, computer):
        self.name = name
        self.player = player
        self.computer = computer
        self.dice = dice

class Dice:
    def __init__(self):
    
    def roll_dice():
        roll = random.randint(1,6)
        return roll()
    pass


class Player:
    def __init__(self):
        self.name = name
        self.turn_score = []
        self.score = 0
    
    def __str__(self):
        return f"{self.name}"

        choice = input("Would you like to (h)old or (r)oll?")
        if choice == 'r':
            self.roll(self.player)
        elif choice == 'h'
            self.hold(self.player)

    def current_sum(self):

    def show_turn_score(self):
        print("Your turn score: ", [f'{current_sum}'])

    def show_total_score(self):
        print("Your score: ", [])

    pass


class Computer:
    def __init__(self):
        self.name = name
        self.turn_score = []
        self.score = score
    
    def __str__(self):
        return f"{self.name}"

    choice = input("Would you like to (h)old or (r)oll?")
    if choice == 'r'
        self.roll(self.computer)
    elif choice == 'h'
        self.hold(self.computer)

    def show_turn_score(self):
        print("Your turn score: ", [])
    
    def show_total_score(self):
        print("Your score: ", [roll])
    pass
