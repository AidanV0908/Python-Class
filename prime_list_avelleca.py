"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 04.5 - Prime List
Date: 06/06/2023

Description:
Utilizing the previous is_prime method, write a list of primes from 2 up to user limit

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
    #Prompt user for limit
    num = int(input("Enter a positive integer: "))
    #Use a for loop, detect all the primes and add to list
    primes = []
    for i in range(2, num):
        if is_prime(i): primes.append(i)
    print(f"The primes up to {num} are: ", end="")
    print(primes[0], end="")
    for prime in primes:
        if (prime != primes[0]):
            print(", ", end="")
            print(prime, end="")
    print("\n", end="")

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