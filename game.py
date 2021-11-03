import time
import sys
from termcolor import colored
from art import visual_elements as art
from os import system
from colors import bcolors
class Game:
    x = colored(art["x"],"red")
    circle = colored(art["circle"],"blue")

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        system("clear")
        print(colored(art["big_logo"],"blue"))
        print(colored(art["xo"],"yellow"))

        while len(self.player1) == 0 :
            player_choice = input(colored("\t\t\t\t\t\tPlayer 1 Choose your side - enter (X or O) : ","green"))
            if player_choice.lower() == "o":
                self.player1 = "o"
                self.player2 = "x"

            elif player_choice.lower() == "x":
                self.player1 = "x"
                self.player2 = "o"
            else:
                print(colored("\t\t\t\t\t\t\t\tInvalid Choice !!!","red"))

        if self.player1 == "o":
            print("Player 1 : ", Game.circle)
            print("Player 2 : ", Game.x)
        else:
            print("Player 1 : ", Game.x)
            print("Player 2 : ", Game.circle)


        for remaining in range(5, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Game begins in: {:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

        system("clear")