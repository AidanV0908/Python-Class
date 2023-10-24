"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 03.4 - Organisms
Date: 05/29/2023

Description:
Given the starting number of a population of organisms and information on how they increase, this program will
return the final population of the organisms

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
    #User inputs starting pop
    pop = float(input("Starting population, in thousands: "))
    #Average daily increase (%)
    p_Aum = float(input("Average daily increase, in percent: "))
    #Num days to multiply
    n_D2M = int(input("Number of days to multiply: "))

    #Print table header
    h1 = "Day"
    h2 = "Approx. Pop"
    print(f"{h1:<3}{h2:>14}")
    #Starting pop
    print(f"{0:3}{pop:14,.3f}")
    #Use a for loop for each day to predict final population
    for i in range(1, n_D2M + 1):
        #Print day and new pop
        pop = pop * (1 + (p_Aum / 100))
        print(f"{i:3}{pop:14,.3f}")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()