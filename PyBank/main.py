#================================================================
# IMPORT THE MODULES & DEFINE THE PATH
#================================================================
#Import Modules
import os
import csv

#Define the path to the csv file based on where this python file is saved
csvpath = os.path.join("03-Python_homework_Instructions_PyBank_Resources_budget_data.csv")

###================================================================
## OPEN & READ THE FILE
###================================================================
### Read the csv file Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    ## CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)  # returns the headers or `None` if the input is empty


    #================================================================
    # WHAT THE HELL AM I DOING?
    #================================================================

    # Create empty lists to put your months and profits and losses in
    date_list = []
    profit_loss_list = []

    # add all the rows to each list by looping through the csv file...
    for row in csvreader:
        #...add each row in the first column (index = 0) to your date_list
        date_list.append(row[0])
        #...and add each row in the second column (index = 1) to your profit_loss_list
        profit_loss_list.append(row[1])

        # TOTAL THE NUMBER OF MONTHS INCLUDED IN THE DATASET
        #-----------------------------------------------------------------
        # Calculate your total months by counting the length of the date_list
        total_months = len(date_list)

        # THE NET TOTAL AMOUNT OF "PROFIT/LOSSES" OVER THE ENTIRE PERIOD
        #-----------------------------------------------------------------
        # convert all items in the profit_loss_list to integers so you can add them together. 
        # Use a comprehension list (list items default to strings)
        profit_loss_list = [int(i) for i in profit_loss_list]
        # calculate the total of the profit_loss_list by summing the column
        total_profit_loss = sum(profit_loss_list)

    # THE AVERAGE OF CHANGES OF "PROFIT/LOSSES" OVER THE ENTIRE PERIOD
    #-----------------------------------------------------------------
    #create empty list to store change values in
    change_list = []
    #set the prev_entry to the first item in the list
    prev_entry = 0
    #print(prev_entry)

    #loop through the profit_loss_list and...
    for current_entry in profit_loss_list:
        #...determine the change by taking the current entry and subtracting the previouis one
       change = current_entry - prev_entry
        #add that change value to the change list
       change_list.append(change)
        #update the prev_entry to the current_entry and continue your loop
       prev_entry = current_entry
    #remove the first entry from the list because there is no prev entry to make a change from
    change_list.pop(0)
    #print(change_list)

    # convert all items in the profit_loss_list to integers so you can add them together. 
    # Use a comprehension list (list items default to strings)
    change_list = [int(entry) for entry in change_list]

    num_of_changes = len(change_list)
    total_of_change = sum(change_list)
    #calculate avg change and round it to only 2 decimal points
    average_change = round((total_of_change / num_of_changes),2)
    #average_change_rounded = round(average_change,2)
    #print(average_change)

    # THE GREATEST INCREASE OF CHANGES OF "PROFIT/LOSSES" OVER THE ENTIRE PERIOD
    #-----------------------------------------------------------------
    greatest_increase_amount = max(change_list)
    #print(greatest_increase_amount)

    # THE GREATEST DECREASE OF CHANGES OF "PROFIT/LOSSES" OVER THE ENTIRE PERIOD
    #-----------------------------------------------------------------
    greatest_decrease_amount = min(change_list)
    #print(greatest_decrease_amount)

    ################## FIGURE OUT WHAT THE DATE IS #######################
    #search for the index of the greatest increase amount within the change_list
    increase_index = change_list.index(greatest_increase_amount)
    ##print(greatest_index)
    #now use the increase_index + 1 (because we took away the first value in the change_list) and find the value in the date_list
    increase_date = date_list[(increase_index+1)]
    #print(greatest_date)

    #repeat the above for the decrease
    decrease_index = change_list.index(greatest_decrease_amount)
    decrease_date = date_list[decrease_index+1]



###================================================================
## PRINT THE ANSWERS TO TERMINAL
###================================================================
    print("""
    ==========================================
                FINANCIAL ANALYSIS
    ==========================================""")
    print(f"    Total Months: {total_months}")
    print(f"    Total: ${total_profit_loss}")
    print(f"    Average Change: ${average_change}")
    print(f"    Greatest Increase in Profits: {increase_date} (${greatest_increase_amount})")
    print(f"    Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_amount}) ")
    print("    ------------------------------------------")

###================================================================
## EXPORT THE RESULTS TO TEXT FILE
###================================================================
#specify the file to write to
output_path =os.path.join("pybank_results.csv")

# Open the file using "write" mode. Specidy the variable to hold its contents
with open(output_path, 'w', newline='') as resultsfile:
        #initialize the csv.writer
        csvwriter = csv.writer(resultsfile, delimiter=',')
        #write first row
        csvwriter.writerow(["FINANCIAL ANALYSIS"])
        csvwriter.writerow(["Total Months",total_months])
        csvwriter.writerow(["Total",f"${total_profit_loss}"])
        csvwriter.writerow(["Greatest Increase in Profits:",f"{increase_date}",f"${greatest_increase_amount}"])
        csvwriter.writerow(["Greatest Decrease in Profits:",f"{decrease_date}",f"${greatest_decrease_amount}"])


