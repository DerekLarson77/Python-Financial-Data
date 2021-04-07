# Module for creating file paths across operating systems.
import os
# Module for reading CSV file.
import csv

# Function that looks for requires our 5 calculations and then writes those answers to a text file.
def file_output(total_votes, net_total, avg_changes, great_profit, great_loss):

# The text file location starts where this main.py is located and then inside folder 'analysis' with the file name 'results'.
    output_path = os.path.join("analysis", "results.txt")

# Opens text file and writes each row line by line.  The '\n' tells the code to write on the next line.
    with open(output_path, 'w', newline='') as txtfile:
        txtfile.write("Election Results")
        txtfile.write('\n' + "---------------------------------")
        txtfile.write('\n' + "Total Votes:  " + str(total_votes))
        txtfile.write('\n' + "---------------------------------")
        txtfile.write('\n' + "Total:  $" + str(net_total))
        txtfile.write('\n' + "Average Change:  $" + str(avg_changes))
        txtfile.write('\n' + "Greatest Increase in Profits:  " + str(great_profit))
        txtfile.write('\n' + "Greatest Decrease in Profits:  " + str(great_loss))


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


print("")
print(candidate_votes)


# Print all values to the terminal.
print("")
print("Election Results")
print("---------------------------------")
print(f"Total Votes:  {total_votes}")
print("---------------------------------")
print(candidates[0])
print(candidates[1])
print(candidates[2])
print(candidates[3])
print("---------------------------------")
#print(f"Winner:  {Winner}")
print("---------------------------------")
print("")

# Calling the file_output function to write to the text file.
#file_output(total_months, net_total, average_change, greatest_increase, greatest_decrease)

