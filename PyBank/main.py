# Module for creating file paths across operating systems.
import os
# Module for reading CSV file.
import csv

# Function that looks for requires our 5 calculations and then writes those answers to a text file.
def file_output(total_months, net_total, avg_changes, great_profit, great_loss):

# The text file location starts where this main.py is located and then inside folder 'analysis' with the file name 'results'.
    output_path = os.path.join("analysis", "results.txt")

# Opens text file and writes each row line by line.  The '\n' tells the code to write on the next line.
    with open(output_path, 'w', newline='') as txtfile:
        txtfile.write("Financial Analysis")
        txtfile.write('\n' + "---------------------------------")
        txtfile.write('\n' + "Total Months:  " + str(total_months))
        txtfile.write('\n' + "Total:  $" + str(net_total))
        txtfile.write('\n' + "Average Change:  $" + str(avg_changes))
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

    ## Variables for index[0] and index[1] of the current row and the previous row.
    net_previous = 0
    net_current = 0
    month_previous = ""
    month_current = ""

    ## Variables for calculating change in profit/loss and then adding up the total.
    change_current = 0
    net_changes = 0
    first = 0
    last = 0


    ## Variables for month and profit/loss of both largest increase and decrease.
    greatest_net_increase = 0
    greatest_month_increase = ""
    greatest_net_decrease = 0
    greatest_month_decrease = ""

    # Read each row in the CSV file.
    for row in csvreader:
        # Add one each time we get to a new row to count months.
        total_months += 1
        # Save the value from net_current from the last row before the variable is updated.
        net_previous = net_current
        # Save the value from month_current from the last row before the variable is updated.
        month_previous = month_current

        # Update net_current to the current row value.
        net_current = int(row[1])
        # Update month_current to the current row value.
        month_current = row[0]

        # An if statement to assign first to the net_current only if nothing has been assigned already.
        if first == 0:
            first = net_current

        change_current = net_current - net_previous

        # If statements to check if the new change needs to be either the new greatest increase or decrease.
        if(change_current > greatest_net_increase):
            greatest_net_increase = change_current
            greatest_month_increase = month_current
        elif(change_current < greatest_net_decrease):
            greatest_net_decrease = change_current
            greatest_month_decrease = month_current

        # Continue to add up the net values of each row.
        net_total += net_current
        net_changes += change_current

# For loop that was going through all the rows of the CSV file ended, so we know net_current is still saving the last row of the file.
last = net_current

# Calculating the average change by taking the total change divided by the total months minus 1, because the first month would be at time 0.
average_change = (last-first) / (total_months - 1)

# Variable for cleaner print statements and to match format needed for function (file_output).
greatest_increase = greatest_month_increase + " ($" + str(greatest_net_increase) + ")"
greatest_decrease = greatest_month_decrease + " ($" + str(greatest_net_decrease) + ")"

# Print all values to the terminal.
print("")
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  {net_total}")
print("Average Change:  $" + str(average_change))
print("Greatest Increase in Profits:  " + greatest_increase)
print("Greatest Decrease in Profits:  " + greatest_decrease)
print("")

# Calling the file_output function to write to the text file.
file_output(total_months, net_total, average_change, greatest_increase, greatest_decrease)

