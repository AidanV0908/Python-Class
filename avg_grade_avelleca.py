"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 06/06/2023

Description:
Enter 5 valid scores, letter grade displayed and average computed

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
    s_List = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        score = get_valid_score()
        grade = determine_grade(score)
        print(f"  The letter grade for {score:.01f} is {grade}.")
        s_List[i] = score
    print("\nResults:")
    average_Score = calc_average(s_List)
    average_Grade = determine_grade(average_Score)
    print(f"  The average score is {average_Score:.2f}.")
    print(f"  The letter grade for {average_Score:.2f} is {average_Grade}.")

def get_valid_score():
    #Enter an infinite while loop that can only be broken by the return statement
    while True:
        #User inputs score
        score = float(input("Enter a score: "))
        #Return score if it is between 0 and 100 inclusive and -1 if the score is not valid, prompting re-entry
        if score <= 100 and score >= 0:
            return score
        else:
            print("  Invalid Input. Please try again.")

def determine_grade(score):
    grade = "F"
    if score >= 64: grade = "D"
    if score >= 73: grade = "C"
    if score >= 82: grade = "B"
    if score >= 92: grade = "A"
    return grade

def calc_average(s_List):
    i = 0
    sum = 0
    while i < len(s_List):
        sum += s_List[i]
        i += 1
    avg = sum / len(s_List)
    return avg
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()