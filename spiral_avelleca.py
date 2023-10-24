"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 06.4 - Spiral
Date: 06/12/2023

Description:
    Draw a spiral described by several functions

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
import math as m
import numpy as np

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    #LOGIC: iterate by accuracy step until x loops. Degrees initially converted to radians for func
    spirals = 6
    step = 1
    pendown()
    for i in range(0, (spirals * 360) + 1, step):
        #GoTo the new position
        goto(x(i), y(i))
    penup()

def x(i):
    i_rad = i * (m.pi / 180)
    return (i / pow(m.pi, 2)) * m.cos(i_rad)

def y(i):
    i_rad = i * (m.pi / 180)
    return (i / pow(m.pi, 2)) * m.sin(i_rad)

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
