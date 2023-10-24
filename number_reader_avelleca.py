"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 08.5 - Number Reader
Date: 06/19/2023

Description:
    Reads the numbers from number writer and calculates data from it including min, max. avg

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
    #Define statistical variables
    max = -sys.maxsize
    min = sys.maxsize
    sum = 0
    #Read file and extrapolate the data
    with open("random_numbers.txt", "r") as f:
        numbers = f.read().split()
        for n in numbers:
            num = int(n)
            sum += num
            if num > max:
                max = num
            if num < min:
                min = num
    #Output
    print(f"{len(numbers)} numbers were read from the file.")
    print(f"Min: {min:,}")
    print(f"Max: {max:,}")
    print(f"Sum: {sum:,}")
    print(f"Avg: {(sum / len(numbers)):,.1f}")
            
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
