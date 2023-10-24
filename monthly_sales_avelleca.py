"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 06/24/2023

Description:
    Given sales data for each month in a year will output a pie chart
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
def collect_sales_data(months):
    data = []
    for month in range(0, len(months)):
       data.append(int(input(f"Enter the sales for {months[month]}: ")))
    return data

def main():
    #A list of all the colors and their respective color codes
    m_colors = {"January":"#4D4038", "February":"#BAA892", "March":"#5B6870", "April":"#6E99B4", "May":"#A3D6D7", 
              "June":"#085C11", "July":"#849E2A", "August":"#C3BE0B", "September":"#E9E45B", "October":"#6B4536",
              "November":"#B46012", "December":"#FF9B1A"}
    #Runs a function to get the sales data (s_data) through user input
    s_data = collect_sales_data(list(m_colors.keys()))
    #Set up the plot
    fig, ax = plt.subplots()
    #Create the pie chart using the s data and the keys and values of the color dictionary as colors and labels
    ax.pie(s_data, colors=list(m_colors.values()), labels=list(m_colors.keys()))
    #Set the title
    ax.set_title('Monthly Sales Values (avelleca)')
    ax.set_xticks([1,2,3,4])
    #Show the plots
    plt.show()


            

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
