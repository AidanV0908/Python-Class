"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 06/12/2023

Description:
Randomizer function generates a random number based on the number of digits it should have.

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
import random as r

"""Write new functions below this line (starting with unit 4)."""


def main():
    #Calls the generate random function passing in digits as parameters
    num1 = random_number(2)
    num2 = random_number(3)
    #Displays the problem
    print(f"  {num1:3}")
    print(f"+ {num2:3}")
    print("-----")
    #Ask user for ans
    u_ans = int(input("= "))
    #Compare answer with real
    if (u_ans == (num1 + num2)):
        print("Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {num1 + num2}.")


def random_number(digits):
    #Random function generates random int in range set by digits
    return r.randint(pow(10, digits - 1), pow(10, digits) - 1)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()