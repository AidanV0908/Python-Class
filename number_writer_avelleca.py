"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 08.4 - Number Writer
Date: 06/19/2023

Description:
    Generates a certain amount of random numbers according to specifications and then returns them

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
def generate_random(count):
    nums = []
    #Generate certain number of random number according to specs
    for i in range(0, count):
        num = r.randint(1119, 1217)
        sum_to_13 = check_sum(num)
        while (sum_to_13 == True):
            num = r.randint(1119, 1217)
            sum_to_13 = check_sum(num)
        nums.append(num)
    return nums

def check_sum(num):
    #Check if the sum of a number is divissible by 13 or not
    num_str = str(num)
    sum = 0
    for n in num_str:
        sum += int(n)
    return sum == 13

        

def main():
    filename = "random_numbers.txt"
    #Ask user for count
    count = int(input("How many numbers would you like? "))
    #Generate a list of numbers of provided count that meet criteria
    numbers = generate_random(count)
    #Write
    with open(filename, "w") as f:
        for n in numbers:
            f.write(f"{n}\n")
    #Msg
    print(f"{count} numbers have been written to {filename}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
