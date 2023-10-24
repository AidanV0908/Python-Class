"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 07.1 - Data Parsing
Date: 06/13/2023

Description:
    Parses data from data on gas prices and presents it. Formats the data in a decadal review with the average inflation adjusted price.

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
import data

"""Write new functions below this line (starting with unit 4)."""

def main():
    i = 0
    year = -1
    sum = 0
    start = data.data[0]
    #Header
    print("          :  Price")
    print("  Decade  : in 2021")
    print("          : Dollars")
    print("-------------------")
    #Check if there are more data sets and that they are complete
    while ((4*i) + 3 <= len(data.data)):
        #Get current data set with i
        cData = data.data[(4*i):(4*i+4)]
        #Update year
        year = cData[0]
        #Add to sum inflation-adj value
        sum += cData[3]
        #If year ends in a 9, do decadal summary and reset average price
        if (year % 10 == 9):
            print(f"{start}{-year} :  ${sum / (year - start + 1):.3f}")
            sum = 0
        elif (year % 10 == 0):
            start = cData[0]
        #Increment i
        i += 1
    #Account for any incomplete decade
    print(f"{start}{-(start + 9)} :  ${sum / (year - start + 1):.3f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
