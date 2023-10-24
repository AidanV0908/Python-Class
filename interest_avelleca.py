"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 01.2 - Interest
Date: 05/21/2023

Description:
    With given interest parameters input by the user, program will run calculation to determine the final output over time

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
    #Request params
    print("Enter the following parameters.")
    #Ask the user for the principal
    p = float(input("  The initial deposit? "))
    #Ask the user for the interest rate in %, divide by 100 for decimal value
    r = float(input("  The annual interest rate in percent? ")) / 100
    #Ask the user for the number of years left in
    t = float(input("  The number of years the account earn interest? "))
    #Ask the user for the time period compounded
    n = float(input("  The number of times interest is compounded each year: "))
    #With the inputs, get the future value
    fv = round(p * pow((1 + (r/n)), n*t), 2)
    #Output the final value
    print(f"The balance of this account will be {fv} after {t} years.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
