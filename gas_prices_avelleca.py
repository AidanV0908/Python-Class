"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 06/24/2023

Description:
    Given text document with average gas prices will create a line chart

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""
def get_gas_prices(filename):
    with open(filename, "r") as f:
        prices = f.read().split()
        return prices

def main():
    #Filename to look for gas prices at
    filename = "2008_Weekly_Gas_Averages.txt"
    #Function that gets the gas prices
    prices = get_gas_prices(filename)
    #Set up the plots
    fig, ax = plt.subplots()
    #Range 1-52 for weeks, prices as y values but neet to be converted to float
    ax.plot(range(1, len(prices) + 1), list(map(float, prices)))
    ax.set_title('2008 Weekly Gas Prices (avelleca)')
    ax.set_xlabel('Weeks (by number)')
    ax.set_ylabel('Average Price (dollars/gallon)')
    ax.set_xlim(1, 52)
    ax.set_ylim(1.5, 4.25)
    ax.grid()
    plt.show()
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
