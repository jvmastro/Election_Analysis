# #The following data needs to be retrived
#     #Total number of votes cast
#     #A complete list of candidates who received votes
#     #Total number of votes each candidate received
#     #Percentage of votes each candidate won
#     #The winner of the election based on popular vote   

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
# with open(file_to_load, "r") as election_data:
#      # To do: perform analysis.
#      print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print header row
    headers = next(file_reader)
    print(headers)
    #    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

# # Using the open() function with the "w" mode we will write data to the file.
# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Counties in the Election\n---------------------------------\nArapahoe\nDenver\nJefferson")