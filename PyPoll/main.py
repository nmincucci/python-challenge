#Import modules
import os
import csv
import pandas as pd

#Define the path to the input CSV file
csvpath = os.path.join("C:/Users/Nick/PythonChallenge/python-challenge/PyPoll/election_data.csv")

#Setting variables for later use
candidate = []
total_votes = 0
candidate_votes = {}

#Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #Read the CSV file
    next(csvreader) #Skips header row              

#Calculate vote totals for each candidate by reading through each row
    for row in csvreader:
        total_votes += 1 #Finds number of total votes cast in the election
        candidate = row[2]
        if candidate in candidate_votes: #Tallies votes for individual candidates
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1 #Creates new candidate when the receieve their first vote

#Find percentage of total votes for each candidate
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        candidate_votes[candidate] = {"percentage": percentage, "votes": votes}

#Compare candidates to each other to determine winner
    winner = max(candidate_votes, key=lambda x: candidate_votes[x]['votes'])
    winning_candidate = winner

#Print results to terminal
print("Election Results")
print("------------------")
print("Total Votes:", total_votes)
print("------------------")
for candidate, data in candidate_votes.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})") #.3f limits the percentage to 3 decimal points
print("------------------")
print(f"Winner: {winning_candidate}")
print("------------------")
print("Analysis results have been exported to 'election_analysis.txt'")

#Write the results to a text file
output_file = "election_analysis.txt"
with open('election_analysis.txt', 'w') as file:
        file.write("Election Analysis\n")
        file.write("------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("------------------\n")
        for candidate, data in candidate_votes.items():
            file.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
        file.write("------------------\n")
        file.write(f"Winner: {winning_candidate}\n")
        file.write("------------------\n")
