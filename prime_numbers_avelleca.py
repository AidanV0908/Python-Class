"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 06/06/2023

Description:
Detect if a number is prime or if it is divisible by anything and then return that to the user,
based on the number that the user entered.

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
    #Prompt user for number
    num = int(input("Enter a positive integer (-1 to quit): "))
    #If not negative 1, determine prime
    while num != -1:
        if is_prime(num):
            print(f"  {num} is prime!")
        else:
            print(f"  {num} is not prime.")
        num = int(input("Enter a positive integer (-1 to quit): "))

#Prime is set to true initially
def is_prime(num):
    prime = True
    #Eliminate special case 0, 1
    if num == 0: prime = False
    if num == 1: prime = False
    #Loop though all numbers that could be multiples
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            prime = False
    return prime



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()