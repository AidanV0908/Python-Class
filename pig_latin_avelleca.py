"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 06/19/2023

Description:
    This script takes a string in Pig Latin and then translates it into regular text by removing the last two letters
    and then moving the third to last letter to the front

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
def pig(pig_str):
    #Separate str into words
    pig_words = pig_str.split(' ')
    words = []
    #Loop through each word
    for pig_word in pig_words:
        #Remove last two letters
        word = pig_word[0:(len(pig_word) - 2)]
        #Third to last to front
        word = word[len(word) - 1] + word[0:len(word) - 1]
        words.append(word)
    #Join and capitalize
    n_str = ' '.join(words).capitalize()
    return n_str

def main():
    in_str = input("Enter a string in Pig Latin: ")
    out_str = pig(in_str)
    print(f"Translation: {out_str}")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
