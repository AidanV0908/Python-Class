"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 02.1 - Leap Year
Date: 05/29/2023

Description:
 If the user provides the program with the year the program will determine whether the month of february
 has 28 or 29 days using the criteria that it is a leap year if the year is divisible by 4 unless the year
 is divisible by 100 and not 400

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
    #Ask the user for the year
    year = int(input("Enter a year: "))
    lY = False
    #Calculate whether it is a leap year or not
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            lY = True
        
    #Output
    if lY:
        print(f"The year {year:} is a leap year.")
        print(f"February of {year:} has 29 days.")
    else:
        print(f"The year {year:} is not a leap year.")
        print(f"February of {year:} has 28 days.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()