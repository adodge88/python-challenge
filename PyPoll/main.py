#================================================================
# IMPORT THE MODULES & DEFINE THE PATH
#================================================================
#Import Modules
import os
import csv

#Define the path to the csv file based on where this python file is saved
csvpath = os.path.join("03-Python_homework_Instructions_PyPoll_Resources_election_data.csv")

###================================================================
## OPEN & READ THE FILE
###================================================================
### Read the csv file Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    ## CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)  # returns the headers or `None` if the input is empty
    #================================================================
    # WHAT I DID :)
    #================================================================
    # Create empty lists to put each column in
    voterID_list = []
    county_list = []
    candidate_list = []

    # add all the rows to each list by looping through the csv file...
    for row in csvreader:
        #...add each row in the first column (index = 0) to your voterID_list
        voterID_list.append(row[0])
        #...add each row in the second column (index = 1) to your county_list
        county_list.append(row[1])
        #...add each row in the third column (index = 2) to your candidate_list
        candidate_list.append(row[2])

    #testeroo
    # print(candidate_list)

        # TOTAL THE NUMBER OF VOTES CAST
        #-----------------------------------------------------------------
        # Calculate your total votes by counting the length of the voterID_list
        total_votes = len(voterID_list)

    # A COMPLETE LIST OF THE CANDIDATES WHO RECEIVED VOTES
    #-----------------------------------------------------------------
    #make an empty list to store the unique candidates in
    unique_candidates = []

    #loop through the complete candidate_list...
    for candidate in candidate_list:
        #...if the candidates name is not already in the unique_candidates list add it, otherwise go to next candidate in loop
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)

    #testeroo
    # print(unique_candidates) printed --> ['Khan', 'Correy', 'Li', "O'Tooley"]

    # THE TOTAL # OF VOTES EACH CANDIDATE WON
    #-----------------------------------------------------------------
    #count the number of votes for each candidate in the list by their index in the list
    khan_votes = candidate_list.count(unique_candidates[0])
    correy_votes = candidate_list.count(unique_candidates[1])
    li_votes = candidate_list.count(unique_candidates[2])
    otoole_votes = candidate_list.count(unique_candidates[3])

    # THE PERCENTAGE OF VOTES EACH CANDIDATE WON
    #-----------------------------------------------------------------
    #calculate the percent of votes for each candidate and round to whole num
    khan_percent = round(khan_votes / total_votes * 100)
    correy_percent = round(correy_votes/ total_votes * 100)
    li_percent = round(li_votes / total_votes * 100)
    otoole_percent = round(otoole_votes / total_votes * 100)

    # THE WINNER OF THE POPULAR VOTE
    #-----------------------------------------------------------------
    #researched a function to find the most frequent entries in the candidate list
    def most_freq(candidate_list):
      return max(set(candidate_list), key=candidate_list.count)
    #print(most_freq(candidate_list))

###================================================================
## PRINT THE ANSWERS TO TERMINAL
###================================================================
print("""
    ==========================================
                ELECTION RESULTS
    ==========================================""")
print(f"    Total Votes: {total_votes}")
print("    ------------------------------------------")
print(f"    {unique_candidates[0]}:     {khan_percent}%     ({khan_votes})")
print(f"    {unique_candidates[1]}:     {correy_percent}%     ({correy_votes})")
print(f"    {unique_candidates[2]}:     {li_percent}%     ({li_votes})")
print(f"    {unique_candidates[3]}:     {otoole_percent}%     ({otoole_votes})")
print("    ------------------------------------------")
print(f"    Winner:     {most_freq(candidate_list)}")

###================================================================
## EXPORT THE RESULTS TO TEXT FILE
###================================================================
#specify the file to write to
output_path =os.path.join("pypoll_results.csv")

# Open the file using "write" mode. Specidy the variable to hold its contents
with open(output_path, 'w', newline='') as resultsfile:
        #initialize the csv.writer
        csvwriter = csv.writer(resultsfile, delimiter=',')
        #write first row
        csvwriter.writerow(["ELECTION RESULTS"])
        csvwriter.writerow(["Total Votes",total_votes])
        csvwriter.writerow([""])
        csvwriter.writerow([unique_candidates[0],f"{khan_percent}%",f"({khan_votes})"])
        csvwriter.writerow([unique_candidates[1],f"{correy_percent}%",f"({correy_votes})"])
        csvwriter.writerow([unique_candidates[2],f"{li_percent}%",f"({li_votes})"])
        csvwriter.writerow([unique_candidates[3],f"{otoole_percent}%",f"({otoole_votes})"])
        csvwriter.writerow([""])
        csvwriter.writerow(["Winner",most_freq(candidate_list)])
