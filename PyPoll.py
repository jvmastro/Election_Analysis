# #The following data needs to be retrived
#     #Total number of votes cast
#     #A complete list of candidates who received votes
#     #Total number of votes each candidate received
#     #Percentage of votes each candidate won
#     #The winner of the election based on popular vote   

# # Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
with open(file_to_load, "r") as election_data:

 # To do: perform analysis.
 print(election_data)

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initalize a total vote counter adn set to zero - Set before we open the file so every time we run the file, total votes starts at zero
total_votes= 0

# Declare a list for canidates 
candidate_options = []

# Declare dictionary for candidate votes
candidate_votes ={}

# Delcare variable to hold an empty string value for the winning candidate, winning count equla to zero, and winning percentage equal to zero
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print candidate name from each row
        candidate_name=row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add it to the list of condidates
            candidate_options.append(candidate_name)

            #Instanitate candidate as a key in dictionary
            candidate_votes[candidate_name] = 0

            #Add candidate votes each time namae appears
        candidate_votes[candidate_name] += 1

# Iterate through candidate list
for candidate_name in candidate_votes:
    
    # Retrive vote count of a candidate
    votes = candidate_votes[candidate_name]

    #calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of # votes to the terminal.
    print(f"{candidate_name} : recieved {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate

    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

     # If true then set winning_count = votes and winning_percent = # vote_percentage.

        winning_count = votes
        winning_percentage = vote_percentage

     # Set the winning_candidate equal to the candidate's name.

        winning_candidate = candidate_name

#Print Winning statement
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


