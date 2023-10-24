"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 05.2 - Spiral
Date: 06/10/2023

Description:
    Move the turtle in a spiral, 45 degree changes, 4 extra pixels per spiral

Contributors:
    Aidan Velleca, avelleca@purdue.edu

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
    setup(564, 564)
    width(5)

def main():
    #Set heading
    setheading(-45)
    #For loop to make this easier - five spirals plus a little extra, 360 / 45 = 8 per spiral + 2 extra = 42
    for i in range(0, 43):
        forward(4 * i)
        left(45)


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
