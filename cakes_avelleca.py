"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 03.1 - Cakes
Date: 05/29/2023

Description:
The user will enter the amount of layers and then a cake will be printed with that size

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
    #Ask the user the amount of layers
    layers = int(input("Enter the number of layers: "))
    #For loop
    for l in range(0, layers):
        str = ""
        #Add spaces
        for i in range(0, layers - l - 1):
            str += " "
        #Open bracket
        str += "["
        #Add stars
        for j in range(0, 2*l + 1):
            str += "*"
        str += "]"
        #Print the final string
        print(f"{str}")


        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()