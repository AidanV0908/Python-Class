"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 05/29/2023

Description:
The user will enter velocity, diameter, and kinematic viscosity and the program will output the Reynold's number

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
    #Ask the user for temp in C
    temp = int(input("Enter the temperature in °C as 5, 20, or 50: "))
    #Get the kinematic viscocity
    k_vis = 0
    if (temp == 5):
        k_vis = 1.52 * pow(10, -6)
    elif (temp == 20):
        k_vis = 1 * pow(10, -6)
    elif (temp == 50):
        k_vis = 5.54 * pow(10, -7)
    
   #Ask for velocity
    v = float(input("Enter the velocity of water in the pipe (m/s): "))
   #Ask for pipe diameter
    d = float(input("Enter the pipe's diameter (m): "))
    #Calculate RE
    Re = (v * d) / k_vis

    #Print answer
    print(f"At {temp:.1f}°C, the Reynolds number for flow at {v} m/s in a {d} m diameter pipe is {Re:.2e}.")

        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()