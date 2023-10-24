"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 05/21/2023

Description:
 If the user provides the program with the number of cookies they 
 want to make then the program will output the amount of each ingredient 
 that they will need

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
    #Ask how many cookies the user wants
    num_Cookies = int(input("How many cookies do you want to make? "))
    #Find how much ingredients one cookie requires
    bPc = 1.25 / 48
    sPc = 1.5 / 48
    fPc = 2.5 / 48
    #Calculate ingredients
    butter = bPc * num_Cookies
    sugar = sPc * num_Cookies
    flour = fPc * num_Cookies
    #Output
    print(f"To make {num_Cookies:,} cookies, you will need:")
    print(f"{butter:10,.2f} cups of butter")
    print(f"{sugar:10,.2f} cups of sugar")
    print(f"{flour:10,.2f} cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()