"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 08.6 - Step Counter
Date: 06/19/2023

Description:
    Reads step.txt and outputs the average number of steps taken each month averaged from the days

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
    filename = "steps.txt"
    print("The average steps taken each month were:")
    #Multidimensional array with #1) name of month, #2) number of days, and #3) average num of steps
    step_data = [["January", 31, 0], ["February", 28, 0], ["March", 31, 0], ["April", 30, 0],
                ["May", 31, 0], ["June", 30, 0], ["July", 31, 0], ["August", 31, 0],
                ["September", 30, 0], ["October", 31, 0], ["November", 30, 0], ["December", 31, 0]]
    with open(filename, "r") as f:
        steps = f.read().split()
        #Keep track of current day in step data
        day = 0
        #Go through each day of each month and add to appropriate
        for month in range(0, len(step_data)):
            m_sum = 0
            for c_day in range(0, step_data[month][1]):
                m_sum += int(steps[day])
                day += 1
            step_data[month][2] = m_sum / step_data[month][1]
        #Print
        for s_dat in step_data:
            print(f"{s_dat[0]:>10} :{s_dat[2]:9.2f}")
            

        





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
