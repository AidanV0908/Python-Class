"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 09.2 - World Series
Date: 06/19/2023

Description:
    Given text document with world series winners in chronological order, will create a search program

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
def load_winners_data():
    filename = "WorldSeriesWinners.txt"
    with open(filename, "r") as f:
        r_series = []
        team_wins = {}
        results = f.read().split("\n")
        year = 1903
        #Make the list for the years and wins and team wins at the same time
        for result in results:
            if (result != ''):
                r_series.append([year, result])
                year += 1
                if (year == 1904 or year == 1994):
                    year += 1
                if (result in team_wins):
                    team_wins[result] += 1
                else:
                    team_wins[result] = 1

        #Convert the list of series results to a dict
        r_series = dict(r_series)

        #Return
        return team_wins, r_series

def main():
    team_wins, r_series = load_winners_data()
    year = int(input("Enter a year in the range 1903 -- 2022: "))
    if (year >= 1903 and year <= 2022):
        if (year in r_series):
            print(f"  The {r_series[year]} won the World Series in {year}.")
            print(f"  They have won the World Series {team_wins[r_series[year]]} times.")
        else:
            print(f"  The World Series wasn't played in the year {year}.")
    else:
        print(f"  Data for the year {year} is not included in this system.")



            

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
