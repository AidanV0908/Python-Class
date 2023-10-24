"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 09.3 - Course Info
Date: 06/19/2023

Description:
    This program contains a dictionary with course info so that when a user looks up a course number the info is returned

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
def get_course_data():
    #Dictionary containing inside dictionaries with all course info if you look up a course
    course_info = {
        "CS101" : {
            "room" : "1461",
            "instructor" : "Django",
            "time" : "9:00 a.m."
        },
        "CS102" : {
            "room" : "4815",
            "instructor" : "Idle",
            "time" : "11:00 a.m."
        },
        "CS103" : {
            "room" : "3634",
            "instructor" : "Rich",
            "time" : "10:00 a.m."
        },
        "NT110" : {
            "room" : "1188",
            "instructor" : "Marshal",
            "time" : "2:00 p.m."
        },
        "CM241" : {
            "room" : "2451",
            "instructor" : "Pickle",
            "time" : "12:00 p.m."
        }
    }

    return course_info
    
def main():
    #Course data got, user inputs course number, out info
    course_data = get_course_data()
    course = input("Enter a course number: ")
    if (course in course_data):
        print(f"  The details for course {course} are:")
        print(f"    Instructor: {course_data[course]['instructor']}")
        print(f"          Room: {course_data[course]['room']}")
        print(f"          Time: {course_data[course]['time']}")
    else:
        print(f"  {course} is an invalid course number.")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
