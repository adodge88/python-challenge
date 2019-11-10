
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
    
    # Total the number of months included in the dataset using a List
    #-----------------------------------------------------------------

    # Create an empty list to put your months in
    date_list = []

    # loop through your csv file and add each row in the first column (0) to your date_list
    for row in csvreader:
        date_list.append(row[0])
        # Calculate your total months by counting the length of the date_list
        total_months = len(date_list)
    # Print your answer :)
    print(f"Total Months: {total_months}")

    

       

    # The net total amount of "Profit/Losses" over the entire period
    
    # The average of changes in of "Profit/Losses" over the entire period

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in losses (date and amount) over the entire period


