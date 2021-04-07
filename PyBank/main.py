# Module for creating file paths across operating systems.
import os
# Module for reading CSV file.
import csv

# Function that looks for requires our 5 calculations and then writes those answers to a text file.
def file_output(total_months, net_total, net_changes, great_profit, great_loss):

# The text file location starts where this main.py is located and then inside folder 'analysis' with the file name 'results'.
    output_path = os.path.join("analysis", "results.txt")

# Opens text file and writes each row line by line.  The '\n' tells the code to write on the next line.
    with open(output_path, 'w', newline='') as txtfile:
        txtfile.write("Financial Analysis")
        txtfile.write('\n' + "---------------------------------")
        txtfile.write('\n' + "Total Months:  " + str(total_months))
        txtfile.write('\n' + "Total:  $" + str(net_total))
        txtfile.write('\n' + "Average Change:  $" + str(net_changes))
        txtfile.write('\n' + "Greatest Increase in Profits:  " + str(great_profit))
        txtfile.write('\n' + "Greatest Decrease in Profits:  " + str(great_loss))

# The CSV file path starts where this main.py is located and then inside folder 'Resources' with file name 'budget_data'.
csvpath = os.path.join("Resources", "budget_data.csv")

# Opening CSV file located in csvpath set prior.
# Csvreader reads the csv file as lists(rows) within lists(columns).
# Delimiter is so python knows what character is separating lists in each row.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Saving the header to a variable before python starts reading down the rows.
    csv_header = next(csvreader)
    #print(f"CSV Header:  {csv_header}")

    # Setting counting variables to zero before any math occurs.
    total_months = 0
    net_total = 0
    net_changes = 0
    greatest_increase = 0
    greatest_decrease = 0

    # Read each row in the CSV file.
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
print("")
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  {net_total}")
print("")

file_output(total_months, net_total, net_changes, greatest_increase, greatest_decrease)

