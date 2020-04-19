# Dependencies
import csv 
import os

# Files to load and output
file_to_load = os.path.join("Resources1", "budget_data1.csv")
file_to_output = os.path.join("analysis1", "Davids_budget_analysis.txt")

# Track various revenue parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# read the csv and convert it to a list of dictionaries 
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        #Track the Totals
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        #Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the Greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"- - - - - - - - - - - - - - - -\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg: .2f}\n"
    f"Greatest Increase In Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease In Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the Output (To terminal)
print(output)

# Export the Results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)