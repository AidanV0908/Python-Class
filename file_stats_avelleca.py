"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 08.3 - File Stats
Date: 06/19/2023

Description:
    Given a file, it will return stats on it's length, how many words it has, and the number of words per line

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
    lines_tot = 0
    words_tot = 0
    filename = 'frontiero_v_richardson.txt'
    with open(filename, 'r') as f:
        #Take the whole file and split around new line characters for lines
        lines = f.read().split('\n')
        for line in lines:
            words = line.split()
            #If there are words on the line (so skip empty) add words and lines to count
            if words != []:
                word_count = len(words)
                words_tot += word_count
                lines_tot += 1
    #Print
    print(f"Total number of words: {words_tot}")
    print(f"Total number of lines: {lines_tot}")
    print(f"Average number of words per line: {words_tot / lines_tot:.1f}")

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
