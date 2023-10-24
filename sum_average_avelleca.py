"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 03.2 - Sum Average
Date: 05/29/2023

Description:
The user will enter multiple numbers and then their sum will be output along with their average

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
    #Start with all variables equal to 0
    num, sum, count = 0, 0, 0
    #Start loop that goes as long as a non-negative number is eentered
    while (num >= 0):
        #Increase count, sum, and num while non-negative
        num = float(input("Enter a non-negative number (negative to quit): "))
        #If this is not the escape number, add to the stats
        if num >= 0:
            count += 1
            sum += num
    #Calculate average if numbers were used
    if count > 0:
        average = sum / count
        #Display stats
        print(f"  You entered {count} numbers.")
        print(f"  Their sum is {sum:.3f} and their average is {average:.3f}.")
    #Else display no numbers entered
    else:
        print("  You didn't enter any numbers.")

        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()