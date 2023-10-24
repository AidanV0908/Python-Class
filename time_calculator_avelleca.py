"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 05/29/2023

Description:
The user will enter a time in seconds and then the program will return
that value in a time format in days, hours, minutes, seconds

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
    #Ask the user for the time
    time_sec = int(input("Please enter a time in seconds: "))
    time_rem = time_sec

    #Less than a minute format
    if time_sec < 60:
        #Print this time
        print(f"  {time_sec} seconds is less than one minute.")
    #Over a minute format
    else:
        #Get d/h/m/s
        #Days
        d = int(time_rem / 86400)
        time_rem -= (d * 86400)
        #Hours
        h = int(time_rem / 3600)
        time_rem -= (h * 3600)
        #Minutes
        m = int(time_rem / 60)
        time_rem -= (m * 60)
        #Seconds
        s = time_rem

        #Print formatting
        #Start
        print(f"  {time_sec:,} seconds equals ", end="")
        #Print any days
        if d >= 1:
            print(f"{d} day(s)", end="")
            #As long as there are more units, add comma
            if (m != 0) or (h != 0) or (s != 0):
                print(", ", end="")
            #If there is only one more type of unit, add the and
            if not(m == 0 and h == 0 and s == 0) and ((m == 0 and h == 0) or (s == 0 and h == 0) or (m == 0 and s == 0)):
                print(f"and ", end="")
        #Print any hours
        if h >= 1:
            print(f"{h} hour(s)", end="")
            #As long as there are more units, add comma
            if (m != 0) or (s != 0):
                print(", ", end="")
            #If there is only one more type of unit, add the and
            if (m == 0 and s != 0) or (s == 0 and m != 0):
                print(f"and ", end="")
        #Print any minutes
        if m >= 1:
            print(f"{m} minute(s)", end="")
            #Since seconds are the only remaining type of units, print the , and if there are seconds
            if (s != 0):
                print(f", and ", end="")
        #Print any seconds
        if s >= 1:
            print(f"{s} second(s)", end="")
        #Print period
        print(".")


        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()