# Module for creating file paths across operating systems.
import os
# Module for reading CSV file.
import csv

def file_output(total_months, net_total):

    output_path = os.path.join("analysis", "results.txt")

    with open(output_path, 'w', newline='') as txtfile:

        txtfile.write(str(total_months))
        txtfile.write(str(net_total))

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

    # Read each row in the CSV file.
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

print(f"Total Months:  {total_months}")
print(f"Total:  {net_total}")

file_output(total_months, net_total)

