"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 06/12/2023

Description:
Randomizer function generates a random number based on the number of digits it should have.

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


def main():
    winner = "tie"
    #Until there is a declared winner, keep playing
    while(winner == "tie"):
        #Get computer's choice
        cC = get_computer_choice()
        pC = get_player_choice()
        #Display choices
        print(f"  The computer chose {cC}, and you chose {pC}.")
        winner = get_winner(cC, pC)
    print("Thanks for playing.")
        

def get_computer_choice():
    #Choose rock paper or scissors at random
    choices = ["rock", "paper", "scissors"]
    return r.choice(choices)

def get_player_choice():
    #Prompt player for choices
    pC = input("Choose rock, paper, or scissors: ")
    while (pC != "rock" and pC != "paper" and pC != "scissors"):
        print("You made an invalid choice. Please try again.")
        pC = input("Choose rock, paper, or scissors: ")
    return pC

def get_winner(cC, pC):
    #Winner variable holds the winner
    winner = "tie"
    if ((pC == "rock" and cC == "scissors") or (pC == "paper" and cC == "rock") or (pC == "scissors" and cC == "paper")):
        print(f"  {pC} beats {cC}")
        print("  You won the game!")
        winner = "player"
    elif ((cC == "rock" and pC == "scissors") or (cC == "paper" and pC == "rock") or (cC == "scissors" and pC == "paper")):
        print(f"  {cC} beats {pC}")
        print("  You lost.  Better luck next time.")
        winner = "computer"
    else:
            print("  It's a tie. Starting over.\n")
    return winner

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()