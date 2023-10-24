"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 04.1 - Falling
Date: 06/06/2023

Description:
Given the amount of time that an object has been falling, the distance that the object has fallen will be returned.

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
    #Iterate through falling times and call function to get the distance
    #Print table header
    h1 = "Time (s)"
    h2 = "Distance (m)"
    print(f"{h1:<10}{h2:>10}")
    print("----------------------")
    #Use a for loop for each day to get distances. 5-50 in increments of 5
    for t in range(5, 51, 5):
        d = falling_dist(t)
        print(f"{t:8}{d:14.1f}")
        

def falling_dist(f_time):
    #Using the falling_time parameter, get the distance fallen
    g = 8.87 #Acceleration constant of Venus
    d = g * pow(f_time, 2) / 2
    return d


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()