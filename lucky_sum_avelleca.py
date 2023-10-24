"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 06/06/2023

Description:
This code will take two input args and sum up all the numbers between the lowest and highest argument divisible by 7
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
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    l_sum = lucky_sum(num1, num2)
    print(f"The sum of the lucky numbers is {l_sum:,}.")

def lucky_sum(num1, num2):
    l_sum = 0
    #Check relation between num1 and num2 to check direction range should go
    if num1 > num2:
        #Set starting num to closest next integer of 7
        starting_num = num2 + (7 - (num2 % 7)) if num2 % 7 != 0 else num2
        #Between starting num and num2, add all multiples of 7
        for i in range(starting_num, num1, 7):
            l_sum += i
    #Same thing as above
    else:
        starting_num = num1 + (7 - (num1 % 7)) if num1 % 7 != 0 else num1
        for i in range(starting_num, num2, 7):
            l_sum += i
    return l_sum


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()