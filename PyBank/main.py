
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
        #...add each row in the first column (0) to your date_list
        date_list.append(row[0])
        #...and add each row in the second column (1) to your profit_loss_list
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

###================================================================
## PRINT THE ANSWERS TO TERMINAL
###================================================================
    print("""
    ==========================================
                FINANCIAL ANALYSIS
    ==========================================""")
    print(f"------Total Months: {total_months}")
    print(f"------Total: ${total_profit_loss}.00")

###================================================================
## EXPORT THE RESULTS TO TEXT FILE
###================================================================
    
        

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in losses (date and amount) over the entire period


