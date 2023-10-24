"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 02.2 - Software Sales
Date: 05/29/2023

Description:
The user will enter the amount of packages that they want to purchase, and then from that a discount
will be applied based on the number of packages

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
    #Ask the user for the packages
    packages = int(input("How many packages will be purchased: "))
    #Discount factor (dF)
    dF = 0

    #Validity check
    if packages > 0:

        #Calculate discount factor
        if packages >= 4:
            dF = 0.1
        if packages >= 40:
            dF = 0.15
        if packages >= 200:
            dF = 0.3
        if packages >= 1000:
            dF = 0.42
            
        #Output
        cost = (1 - dF) * packages * 880
        if dF == 0:
            print("  No discount applied.")
        else:
            print(f"  {dF * 100:.0f}% discount applied.")
        print(f"  The total price to purchase {packages:} packages is ${cost:,.2f}.")
    
    else:
        print("  Invalid Input!")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()