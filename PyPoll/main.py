# Module for creating file paths across operating systems.
import os
# Module for reading CSV file.
import csv

# Function that looks for requires our 5 calculations and then writes those answers to a text file.
def file_output(total_votes, candidates, votes_per, candidate_votes, winner, vote_winner):

# The text file location starts where this main.py is located and then inside folder 'analysis' with the file name 'results'.
    output_path = os.path.join("analysis", "results.txt")

# Opens text file and writes each row line by line.  The '\n' tells the code to write on the next line.
    with open(output_path, 'w', newline='') as txtfile:
        txtfile.write("Election Results")
        txtfile.write('\n' + "---------------------------------")
        txtfile.write('\n' + "Total Votes:  " + str(total_votes))
        txtfile.write('\n' + "---------------------------------")

        for i in range(len(candidates)):
            txtfile.write('\n' + candidates[i] + ": " + str(votes_per[i]) + "%  (" + str(candidate_votes[i]) + ")")

        txtfile.write('\n' + "---------------------------------")
        txtfile.write('\n' + "Winner:  " + winner + "!")
        txtfile.write('\n' + "With " + str(vote_winner) + " votes!")
        txtfile.write('\n' + "---------------------------------")


def candidate_checker(name, candidates):
    if candidates == []:
        candidates.append(name)
    else:
        for candidate in candidates:
            if name == candidate:
                return
        candidates.append(name)


# The CSV file path starts where this main.py is located and then inside folder 'Resources' with file name 'budget_data'.
csvpath = os.path.join("Resources", "election_data.csv")

# Opening CSV file located in csvpath set prior.
# Csvreader reads the csv file as lists(rows) within lists(columns).
# Delimiter is so python knows what character is separating lists in each row.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Saving the header to a variable before python starts reading down the rows.
    csv_header = next(csvreader)
    #print(f"CSV Header:  {csv_header}")

    # Setting counting variables to zero before any math occurs.
    csv_array = []
    total_votes = 0
    i = 0
    candidates = []
    candidate_votes = []
    votes_per = []
    vote_winner = 0

    # Read each row in the CSV file.
    for row in csvreader:
        # Add one each time we get to a new row to count months.
        csv_array.append(row)
        total_votes += 1
        name = row[2]
        candidate_checker(name, candidates)


    for candidate in candidates:
        i += 1
        candidate_votes.append(0)
        for row in csv_array:
            name = row[2]
            if str(candidate) == str(name):
                candidate_count = candidate_votes[i-1] + 1
                candidate_votes[i-1] = candidate_count
        if candidate_votes[i-1] > vote_winner:
            vote_winner = candidate_votes[i-1]
            winner = candidate
        votes_per.append(round(candidate_votes[i-1]/total_votes * 100, 3))



# Print all values to the terminal.
print("")
print("Election Results")
print("---------------------------------")
print(f"Total Votes:  {total_votes}")
print("---------------------------------")

for i in range(len(candidates)):
    print(candidates[i] + ": " + str(votes_per[i]) + "%  (" + str(candidate_votes[i]) + ")")

print("---------------------------------")
print(f"Winner:  {winner}!")
print(f"With {vote_winner} votes!")
print("---------------------------------")
print("")

# Calling the file_output function to write to the text file.
file_output(total_votes, candidates, votes_per, candidate_votes, winner, vote_winner)

