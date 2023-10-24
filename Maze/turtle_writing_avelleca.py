"""
Author: Aidan  Velleca, avelleca@purdue.edu
Assignment: 05.4 - Turtle Writing
Date: 06/11/2023

Description:
    A script that writes "Hammer Down" using the turtle

Contributors:
    N/A

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    color("purple")


def draw_D():
    """Write this function."""
    setheading(90)
    forward(50)
    setheading(0)
    for i in range(0, 50):
        forward(3.14 / 2)
        right(180 / 50)
    


def draw_H():
    """Write this function."""
    setheading(90)
    forward(50)
    setheading(270)
    penup()
    forward(25)
    pendown()
    setheading(0)
    forward(20)
    setheading(90)
    forward(25)
    setheading(270)
    penup()
    forward(25)
    pendown()
    forward(25)

def draw_a():
    """Write this function."""
    penup()
    setheading(0)
    forward(25)
    setheading(90)
    forward(12)
    pendown()
    circle(12)
    penup()
    forward(12)
    pendown()
    setheading(270)
    forward(25)

def draw_e():
    """Write this function."""
    setheading(0)
    penup()
    forward(25)
    setheading(90)
    forward(3.14)
    setheading(215)
    pendown()
    for i in range(0, 25):
        forward(3.14)
        right(315 / 25)
    setheading(180)
    forward(25)
    penup()
    setheading(0)
    forward(25)
    setheading(270)
    forward(10)
    pendown()




def draw_m():
    """Write this function."""
    for i in range(0, 2):
        setheading(90)
        forward(18)
        for i in range(0, 12):
            forward(3.14 / 2)
            right(180 / 12)
        forward(18 + (3.14 / 2))


def draw_n():
    """Write this function."""
    setheading(90)
    forward(18)
    for i in range(0, 12):
        forward(3.14)
        right(180 / 12)
    forward(18 + (3.14 / 2))

def draw_o():
    """Write this function."""
    penup()
    setheading(0)
    forward(50)
    setheading(90)
    forward(12)
    pendown()
    circle(12)
    penup()
    setheading(270)
    forward(12)
    pendown()

def draw_r():
    """Write this function."""
    setheading(90)
    forward(20)
    for i in range(0, 20):
        right(180 / 20)
        forward(3.14 / 2)
    penup()
    forward(20)
    pendown()

def draw_w():
    """Write this function."""
    setheading(90)
    penup()
    forward(25)
    pendown()
    for i in range(0, 2):
        setheading(300)
        forward(25)
        setheading(60)
        forward(25)
    penup()
    setheading(270)
    forward(25)
    pendown()

def letter_space():
    penup()
    setheading(0)
    forward(10)
    pendown()

def main():
    """After these lines, call your letter drawing functions as needed to draw
    the words "Hammer Down".
    """
    goto(0,0)
    #Draw all the letters
    draw_H()
    letter_space()
    draw_a()
    letter_space()
    draw_m()
    letter_space()
    draw_m()
    letter_space()
    draw_e()
    letter_space()
    draw_r()
    penup()
    goto(0, -70)
    pendown()
    #Draw all the letters for "down"
    draw_D()
    letter_space()
    draw_o()
    letter_space()
    draw_w()
    letter_space()
    draw_n()

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
