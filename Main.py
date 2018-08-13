'''
    Title:          A simple Turtle Race Game
    Author:         Daljeet Singh Chhabra
    Language:       Python
    Date Created:   13-08-2018
    Last Modified:  13-08-2018
'''

from turtle import *
from random import randint
import time


class Game:
    def __init__(self):
        self.color = ["red", "white", "blue", "yellow"]     # List of turtle colors
        self.turt = []                                      # list name turt
        self.x = 0

    def path(self):
        for i in range(14):
            pencolor("white")  # Loop for making lanes
            write(i)
            right(90)
            forward(10)
            pendown()
            forward(150)
            penup()
            backward(160)
            left(90)
            forward(20)
            if i == 20:
                x, y = position()                           # To find position of last lane and store it in x,y
                self.x = x
                penup()
                ht()                                        # To hide the sign of turtle
        pendown()

    def positionTurtle(self):
        y = 230
        for i in range(4):
            self.turt.append(Turtle())                      # Placing the turtles on starting line
            self.turt[i].right(360)
            self.turt[i].color(self.color[i])
            self.turt[i].shape("turtle")
            self.turt[i].penup()
            self.turt[i].goto(-270, y)
            y = y - 40
            self.turt[i].pendown()

    def countdown(self):
        w = Turtle()
        w.color("black")
        w.penup()
        w.goto(0, 10)
        w.pendown()
        w.write("3", move=False, align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        w.clear()
        w.write("2", move=False, align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        w.clear()
        w.write("1", move=False, align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        w.clear()
        w.write("Go", move=False, align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        penup()

    def move(self):
        for i in range(140):
            self.turt[0].forward(randint(1, 5))             # To move Turtles at random speed
            a, b = self.turt[0].position()
            if self.x <= a:                                 # To check the Winner
                self.turt[0].right(360)
                ht()
                penup()
                goto(0, -70)
                pendown()
                pencolor("red")
                write("Red Colour Turtle won the game", move=False, align="center",
                      font=("Times Roman New", 25, "normal"))
                break

            self.turt[1].forward(randint(1, 5))
            a, b = self.turt[1].position()
            if self.x <= a:
                self.turt[1].right(360)
                ht()
                penup()
                goto(0, -70)
                pendown()
                pencolor("white")
                write("White Colour Turtle won the game", move=False, align="center",
                      font=("Times Roman New", 25, "normal"))
                break
            self.turt[2].forward(randint(1, 5))
            a, b = self.turt[2].position()
            if self.x <= a:
                self.turt[2].right(360)
                ht()
                penup()
                goto(0, -70)
                pendown()
                pencolor("blue")
                write("Blue Colour Turtle won the game", move=False, align="center",
                      font=("Times Roman New", 25, "normal"))
                break
            self.turt[3].forward(randint(1, 5))
            a, b = self.turt[3].position()
            if self.x <= a:
                ht()
                self.turt[3].right(360)
                penup()
                goto(0, -70)
                pendown()
                pencolor("Yellow")
                write("Yellow Colour Turtle won the game", move=False, align="center",
                      font=("Times Roman New", 25, "normal"))
                break


def main():
    # Setting the window
    sc = Screen()
    sc.bgcolor("green")  # Setting the Background to Green
    penup()
    goto(-250, 250)

    # Object declaration of the class Game
    ob = Game()

    # Function Calls for the Race
    ob.path()
    ob.positionTurtle()
    ob.countdown()
    ob.move()

    done()


main()
