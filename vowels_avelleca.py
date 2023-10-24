"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 06/12/2023

Description:
    Draws each of the vowels based on the randomizer

Contributors:
    Name, login@purdue.edu [repeat for each]

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


def draw_a():
    """Write this function."""
    penup()
    setheading(0)
    forward(50)
    setheading(90)
    forward(25)
    pendown()
    circle(25)
    penup()
    forward(25)
    pendown()
    setheading(270)
    forward(50)
    penup()
    setheading(0)
    forward(30)
    pendown()



def draw_e():
    """Write this function."""
    setheading(0)
    penup()
    forward(50)
    setheading(90)
    forward(3.14 * 2)
    setheading(215)
    pendown()
    for i in range(0, 25):
        forward(3.14 * 2)
        right(315 / 25)
    setheading(180)
    forward(50)
    penup()
    setheading(0)
    forward(50)
    setheading(270)
    forward(20)
    setheading(0)
    forward(30)
    pendown()



def draw_i():
    """Complete this function to draw the character i."""
    pendown()
    setheading(90)
    forward(50)
    penup()
    forward(25)
    dot(5)
    setheading(270)
    forward(75)
    setheading(0)
    forward(30)
    pendown()


def draw_o():
    """Write this function."""
    penup()
    setheading(0)
    forward(50)
    setheading(90)
    forward(25)
    pendown()
    circle(25)
    penup()
    setheading(270)
    forward(25)
    penup()
    setheading(0)
    forward(30)
    pendown()


def draw_u():
    """Complete this function to draw the character u."""
    penup()
    setheading(90)
    forward(50)
    pendown()
    setheading(270)
    forward(25)
    for i in range(0, 25):
        left(180 / 25)
        forward(3.14)
    forward(25 - 3.14)
    setheading(270)
    forward(50)
    penup()
    setheading(0)
    forward(30)
    pendown()


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    pass


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
