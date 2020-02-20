import random


class Game:
    def __init__(self):
        self.player = Player("Player")
        self.computer = Computer("Computer")
        self.dice = Dice()
    
    def play(self):
        first = random.randint(0,1)
        if first == 0:
            print("Computer goes first")
            self.computer_turn()
        else:
            print("Player goes first")
            self.player_turn()
        return first

    def player_turn(self):
        self.player.player_turn = 0
        choice = "r"
        while choice == "r":
            self.player.turn_score += self.dice.roll()
            choice = input("Would you like to (r)oll or (h)old?")
        self.player.score += self.player.turn_score 
        self.computer_turn()

    def computer_turn(self):
        self.computer.turn_score = 0
        while self.computer.turn_score < 20:
            self.computer.turn_score += self.dice.roll()
        self.computer.score += self.computer.turn_score
        self.player_turn()
        

class Dice:

    def roll(self):
        roll = random.randint(1, 6)
        print(roll)
        return roll
   


class Player:
    def __init__(self, name):
        self.name = name
        self.turn_score = 0
        self.score = 0
    
    def __str__(self):
        return f"{self.name}"

        

    def show_turn_score(self):
        print("Your turn score: ", f'{self.turn_score}')

    def show_total_score(self):
        print("Your score: ", f'{self.score}')




class Computer:
    def __init__(self, name):
        self.name = name
        self.turn_score = 0
        self.score = 0
    
    def __str__(self):
        return f"{self.name}"


    def show_turn_score(self):
        print("Your turn score: ", f'{self.turn_score}')
    
    def show_total_score(self):
        print("Your score: ", f'{self.score}')
    


game = Game()
game.play()
