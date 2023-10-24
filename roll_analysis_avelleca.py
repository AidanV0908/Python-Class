"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 06/18/2023

Description:
    Rolls two dice a specified amount of times and returns a summary of the results

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
    rolls = 1000000
    results = get_2d6_rolls(rolls)
    #Count for each number
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #Iterate through each result and iterate the count for whatever that is by 1
    for result in results:
        counts[(result - 2)] += 1
    #Print the counts
    print("Roll  Frequency")
    iterator = 2
    for count in counts:
        print(f"{iterator:3}    {(count/rolls) * 100:5.2f}%")
        iterator += 1

def roll_d6():
    return r.randint(1, 6)

def get_2d6_rolls(times):
    l_rolls = []
    for i in range(0, times):
        sum = roll_d6()
        sum += roll_d6()
        l_rolls.append(sum)
    return l_rolls

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
