"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 06/19/2023

Description:
    This program will read a file with state capitals and make a dictionary from them to test the user on state capitals

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
import random as r

"""Write new functions below this line (starting with unit 4)."""
def get_state_data():
    #Filename
    filename = "state_capitals.txt"
    #Create dictionary
    capitals_dict = {}
    #Read from file
    with open(filename, "r") as f:
        capitals = f.read().split("\n")
        for capital in capitals:
            c = capital.split(", ")
            #Check for exceptions
            if (len(c) >= 2):
                capitals_dict[c[1]] = c[0]
    #Return dict
    return capitals_dict

def main():
    #Get capitals
    caps = get_state_data()
    #Continue variable
    cont = True
    #Correct
    correct = 0
    #Done
    done = 0
    #Incorect capitals
    i_caps = []
    #Quiz
    while cont and len(caps) > 0:
        #Incorrect list to be asked at end
        #Choose random key-val pair
        state, capital = r.choice(list(caps.items()))
        #Pop it from the dict so that it won't be asked again
        caps.pop(state)
        answer = input(f"What is the capital of {state} (enter 0 to quit)? ")
        if (answer != "0"):
            if (answer.lower() == capital.lower()):
                print("  That is correct!")
                correct += 1
            else:
                print("  That is incorrect.")
                print(f"  The capital of {state} is {capital}.")
                i_caps.append([state, capital])
            done += 1
        else:
            cont = False
        if (len(caps) == 0):
            caps = dict(i_caps)
            i_caps.clear()
    if (done != 0):
        print(f"You answered {correct/done * 100:.1f}% of the questions correctly.")
    else:
        print("You didn't answer any questions.")

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
