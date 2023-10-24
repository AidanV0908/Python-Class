"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 06/12/2023

Description:
    This program uses the turtle to draw the five vowels in a random order

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels
import random as r

"""Write new functions below this line (starting with unit 4)."""


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
    #List of five vowels
    vowels_l = ["a", "e", "i", "o", "u"]
    #While this list has elements...
    while (len(vowels_l) > 0):
        #Choose one at random
        rand_vowel = r.choice(vowels_l)
        #Draw the associated letter
        if(rand_vowel == "a"):
            vowels.draw_a()
        elif(rand_vowel == "e"):
            vowels.draw_e()
        elif(rand_vowel == "i"):
            vowels.draw_i()
        elif(rand_vowel == "o"):
            vowels.draw_o()
        else:
            vowels.draw_u()
        #Remove it from the list so it's not repeated
        vowels_l.remove(rand_vowel)



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
