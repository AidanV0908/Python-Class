"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 06/11/2023

Description:
    The user will enter the number of points on the star and then the program will draw and complete it.

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
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    #User inputs point
    points = int(input("Enter the number of points on the star: "))
    #Colors
    color('red', 'blue')
    #Set inner and outer angles
    i_angle = 360 / points
    o_angle = 2 * i_angle
    #Set init
    init_angle = -90 + o_angle / 2
    setheading(init_angle)
    #Start filling
    begin_fill()
    #Run the loop
    for i in range(0, points):
        forward(60)
        left(180 - i_angle)
        forward(60)
        right(180 - o_angle)
    #End fill
    end_fill()
    #Return init
    setheading(init_angle)


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
