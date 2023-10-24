"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 09.4 - File Analysis
Date: 06/19/2023

Description:
    Creates a file outputting the frequency of words in two text documents, as well as a file with lists of words
    in both docs and only one doc

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
import string

"""Write new functions below this line (starting with unit 4)."""
def word_process(filename):
    words = {}
    with open(filename, "r") as f:
        #Read
        words = f.read().split()
        #Remove leading and trailing whitespace, punctuation from each word
        for i in range(0, len(words)):
            words[i] = words[i].strip(string.punctuation).lower()
        #Puts words in dict
        d_of_words = {}
        for word in words:
            if word in d_of_words:
                d_of_words[word] += 1
            else:
                d_of_words[word] = 1
        sorted_d_of_words = dict(sorted(d_of_words.items()))
        return sorted_d_of_words
    
#All of these functions deal with converting to file or finding words in common / different
def dict_to_file(filename, i_dict):
    with open(filename, "w") as f:
        for k, v in i_dict.items():
            f.write(f"{k}: {v}\n")

def common_words(dict1, dict2):
    common = []
    for k in dict1:
        if (k in dict2):
            common.append(k)
    return sorted(common)

def e_but_not_b(dict1, dict2):
    either = []
    for k in dict1:
        if (k not in dict2):
            either.append(k)
    for k in dict2:
        if (k not in dict1):
            either.append(k)
    return sorted(either)

def list_to_file(filename, list):
    with open(filename, "w") as f:
        for e in list:
            f.write(f"{e}\n")


def main():
    #Save file names for quick reference
    file1 = "python_1.txt"
    file2 = "python_2.txt"
    out_py1 = "python_1_word_frequency.txt"
    out_py2 = "python_2_word_frequency.txt"
    out_both = "common_words.txt"
    out_either = "eitherbutnotboth.txt"
    #Get words from file 1
    words1 = word_process(file1)
    words2 = word_process(file2)
    #Output to file
    dict_to_file(out_py1, words1)
    dict_to_file(out_py2, words2)
    #Create common words
    common = common_words(words1, words2)
    #Either but not both
    either = e_but_not_b(words1, words2)
    #Print these to their respective lists
    list_to_file(out_both, common)
    list_to_file(out_either, either)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
