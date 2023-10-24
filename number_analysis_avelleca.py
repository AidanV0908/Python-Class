"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 06/16/2023

Description:
    Creates a list of numbers and then gives the highest, lowest, total, and average of the list

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
import sys

"""Write new functions below this line (starting with unit 4)."""

def main():
    #Get and return list
    print(f"Enter 10 numbers:")
    nums = get_number_list()
    #Define the max and min numbers and make them be replaced as appropriate as new nums entered
    high = -sys.maxsize
    low = sys.maxsize
    tot = 0
    for i in range(0, 10):
        #Analysis
        entry = nums[i]
        if (entry < low):
            low = entry
        if (entry > high):
            high = entry
        tot += entry
    #Out
    print(f"Highest number: {high:.2f}")
    print(f"Lowest number: {low:.2f}")
    print(f"Total: {tot:.2f}")
    print(f"Average: {(tot / 10):.2f}")

def get_number_list():
    nums = []
    for i in range(0, 10):
        #Entry
        entry = float(input(f"  number {(i+1):2} of 10: "))
        nums.append(entry)
    return nums

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
