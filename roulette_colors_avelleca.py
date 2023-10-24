"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 05/29/2023

Description:
The user will enter the pocket of the roulette wheel and the program will return the 
color of the pocket that the roullete wheel lands on. The 0 pocket is green, the others
have a different alternating even / odd pattern of red and black

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    #Ask the user for the pocket
    pocket = int(input("Please choose a pocket number: "))
    #Color string variable
    color = "none"

    #Validity check
    if pocket >= 0 and pocket <= 36:
        #If it is a valid pocket, assign color
        if pocket == 0:
            color = "green"
        elif (pocket > 0 and pocket <= 10) or (pocket > 18 and pocket <= 28):
            if pocket % 2 == 0:
                color = "black"
            else:
                color = "red"
        else:
            if pocket % 2 == 0:
                color = "red"
            else:
                color = "black"

        #Print this color
        print(f"  Pocket number {pocket} is {color}.")

    else:
        print("  Invalid Input!")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()