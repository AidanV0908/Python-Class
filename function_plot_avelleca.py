"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 10.4 - Function Plot
Date: 06/25/2023

Description:
    Plots two functions using matplotlib: (5sinx)^2 - 10 and 10cos(x^2) + x^2 - 20

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
import math as m
import numpy as np

"""Write new functions below this line (starting with unit 4)."""
def main():
    fig, ax = plt.subplots()
    #The limits of the graph, define variables
    N = 2*m.pi
    u = np.arange(0, N, m.pi / pow(2, 16))
    x, y1, y2 = [], [], []
    #Set the x values and appropriate y values
    for n in u:
        x.append(n)
        y1.append(pow(5*m.sin(n), 2) - 10)
        y2.append(10 * m.cos(pow(n, 2)) + pow(n, 2) - 20)
    #Set colors
    ax.plot(x, y1, 'g')
    ax.plot(x, y2, color='b')
    x_label_vals = [m.pi/2, m.pi, 3*m.pi/2, 2*m.pi]
    #Label the axes
    x_labels = [r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"]
    ax.legend([r'$(5\sin{x})^2 - 10$', r'$10\cos{(x^2)} + x^2 - 20$'], loc='lower right')
    ax.set_yticks([-20, -10, 10, 20])
    ax.set_title("10.4 Function Plot (avelleca)")
    #Create ticks
    ax.set_xticks(x_label_vals)
    ax.set_xticklabels(x_labels)
    #Splines
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
