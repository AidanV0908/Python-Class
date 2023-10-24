"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 07.4 - Magic Square
Date: 06/18/2023

Description:
    Check if a 3x3 grid of numbers is a Lo Shu Magic Square

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
    #Run all the squares
    s_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s_2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    s_3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    #Output results
    out_result(s_1)
    print("")
    out_result(s_2)
    print("")
    out_result(s_3)

def print_square(square):
    #Print squares
    print(f"  {square[0][0]} {square[0][1]} {square[0][2]}")
    print(f"  {square[1][0]} {square[1][1]} {square[1][2]}")
    print(f"  {square[2][0]} {square[2][1]} {square[2][2]}")

def is_magic(square):
    magic = True
    #Check sums
    for i in range(0, 2):
        if (square[i][0] + square[i][1] + square[i][2] != 15) or (square[0][i] + square[1][i] + square[2][i] != 15):
            magic = False
    if (square[0][0] + square[1][1] + square[2][2] != 15) or (square[2][0] + square[1][1] + square[0][2] != 15):
        magic = False
    #Check if all numbers 1-9 are contained in the square
    for num in range(1, 10):
        contains_num = False
        #For loop checking each element of each row and column
        for i in range(0, 3):
            for j in range(0, 3):
                if (square[i][j] == num):
                    contains_num = True
        if (contains_num == False):
            magic = False
    #Return
    return magic


def out_result(square):
    #Do all output formatting
    print("Your square is:")
    print_square(square)
    #If it is a magic square, say so, if not, print that
    if (is_magic(square)):
        print("It is a Lo Shu magic square!")
    else:
        print("It is not a Lo Shu magic square.")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
