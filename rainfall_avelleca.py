"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 03.3 - Rainfall
Date: 05/29/2023

Description:
The user will enter rainfall data over a specified range of years of their choosing for each month and
then the average and total rainfall will be returned to them.

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
    #User inputs years
    years = int(input("Enter the number of years: "))
    #Array for the months so they can be called in for
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    t_Fall = 0
    #Check valid year amount
    if years <= 0:
        print("Invalid input; years must be greater than 0.")
    else:
        #Loop years
        for i in range(0, years):
            print(f"  For year No. {i + 1}")
            #Loop months
            for i in range(0, 12):
                #Add to rainfall if value is non-negative
                fall = -1
                while(fall < 0):
                    fall = float(input(f"    Enter the rainfall for {months[i]}.: "))
                    if fall < 0:
                        print("    Invalid input; rainfall cannot be negative.")
                t_Fall += fall
        #Output
        print(f"There are {years*12} months.")
        print(f"The total rainfall was {t_Fall:.2f} inches.")
        print(f"The monthly average rainfall was {t_Fall / (years * 12):.2f} inches.")
        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()