#PyBank Analysis

import csv
import os


file_to_load = os.path.join("Resources", "budget_data.csv")

file_to_save = os.path.join("analysis","budget_analysis.txt")

date = []
monthly_changes = []
profit_loss = []


net_total = 0
total_change_profit = 0
initial_profit = 0


greatest_profit_amount = 0
greatest_loss = 0


total_months = 0

with open(file_to_load) as budget_data:

    csv_reader = csv.reader(budget_data)

    headers = next(csv_reader)

    for row in csv_reader:

        total_months += 1

        date.append(row[0])


        final_profit = float(row[1])
        change = final_profit - initial_profit

        net_total = net_total + change


        monthly_changes.append(change)

        total_change_profit = total_change_profit + change
        initial_profit = final_profit
        
        sum_profit_loss = sum(monthly_changes)
        average_change_monthly = (sum_profit_loss/total_months)
        avg_change = sum(monthly_changes[1:]) / total_months

        greatest_profit_amount = max(monthly_changes)
        greatest_loss = min(monthly_changes)

        greatest_profit_date = date[monthly_changes.index(greatest_profit_amount)]
        greatest_loss_date = date[monthly_changes.index(greatest_loss)]
        

    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profits: " + "$" + str(int(net_total)))
    print("Average Change: " + "$" + str(round(sum(monthly_changes[1:]) / (total_months - 1),2)))
    print("Greatest Increase in Profits: " + str(greatest_profit_date) + " ($" + str(greatest_profit_amount) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_loss_date) + " ($" + str(greatest_loss)+ ")")
    print("----------------------------------------------------------")

with open(file_to_save, 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + str(int(net_total)) +"\n")
    text.write("    Average Change: " + '$' + str(round(sum(monthly_changes[1:]) / (total_months - 1),2)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(greatest_profit_date) + " ($" + str(greatest_profit_amount) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(greatest_loss_date) + " ($" + str(greatest_loss) + ")\n")
    text.write("----------------------------------------------------------\n")



