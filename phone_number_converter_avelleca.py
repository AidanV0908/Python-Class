"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 06/19/2023

Description:
    Given a phone number with letters, this script will convert the letters into numerical digits

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
def convert_number(number):
    #Convert number to upper
    number = number.upper()
    #An array for all the converted nums of the original
    arr_nums = []
    #Go through each number and convert it if it matches any of the conversion cases
    for c in number:
        if c == 'A' or c == 'B' or c == 'C':
            c = '2'
        elif c == 'D' or c == 'E' or c == 'F':
            c = '3'
        elif c == 'G' or c == 'H' or c == 'I':
            c = '4'
        elif c == 'J' or c == 'K' or c == 'L':
            c = '5'
        elif c == 'M' or c == 'N' or c == 'O':
            c = '6'
        elif c == 'P' or c == 'Q' or c == 'R' or c == 'S':
            c = '7'
        elif c == 'T' or c == 'U' or c == 'V':
            c = '8'
        elif c == 'W' or c == 'X' or c == 'Y' or c == 'Z':
            c = '9'
        #Append the new character to the array
        arr_nums.append(c)
    new_number = ''.join(arr_nums)
    return new_number

def main():
    number = input("Enter a telephone number: ")
    print(f"  {number}")
    c_number = convert_number(number)
    print(f"  {c_number}")

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
