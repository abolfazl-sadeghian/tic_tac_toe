import time
import sys
from termcolor import colored
from art import visual_elements as art
from art import x as x_lst
from art import circle as circle_lst
from art import board as board
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


        for remaining in range(1, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Game begins in: {:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

        system("clear")

    def draw_table(self):
        print()
        print()
        # for i in range(1,18):
        #     for y in range(1,3):
        #         print("\t\t|")
        #         self.draw_x()
        #     if(i>0 and i % 6 == 0):
        #         print("\t\t------------------------------------------------")
        num = 1
        if num == 1:
            iOffset = 0
            jOffset = 0
        if num == 2:
            iOffset = 0
            jOffset = 16
        if num == 3:
            iOffset = 0
            jOffset = 32
        if num == 4:
            iOffset = 9
            jOffset = 0
        if num == 5:
            iOffset = 9
            jOffset = 16
        if num == 6:
            iOffset = 9
            jOffset = 32
        if num == 7:
            iOffset = 17
            jOffset = 0
        if num == 8:
            iOffset = 17
            jOffset = 16
        if num == 9:
            iOffset = 17
            jOffset = 32

        for i in range(iOffset, iOffset + 7):
            for j in range(jOffset, jOffset + 14):
                board[i + 1][j] = circle_lst[i - iOffset][j - jOffset]

        print()
        print()

    def draw_x(self):
       for line in x_lst:
           for item in line:
               print(item,end="")
           print()

    def draw_circle(self):
        for line in circle_lst:
            for item in line:
                print(item, end="")
            print()

