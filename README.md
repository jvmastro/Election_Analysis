<h1 align="center"> Colorado Congressional Election Audit</h1>

## Overview of Assignment 
A Colorado Board of Elections employee needs the results of a local congressional election to be audited. The following are to be calculated:

* Total votes cast 
* Number of votes cast in each county
* Percentage of votes placed in each county
* County with the highest voter turnout
* Total number of votes each candidiate received 
* Percentage of votes each candidate won 
* Winnner of the election based popular vote


## Resources 
- Data Source: [Election Results](Resources/election_results.csv)
- Software: Python 3.6.6, Visual Studio Code 1.38.1

## Audit Results and Supporting Code Examples

*Results and explanations reference the code detailed fully in [PyPoll Code](PyPoll_Challenge.py)*

<h3 aling="center"> Results</h3>

<p align="center">
  <img width="372" height="395" src= images/election_results_image.png>
</p>
    
  <h3 aling="center"> Supporting Code Examples</h3>

  
 * To calculate the total votes cast, tally the votes by candiate, and count the votes by county:
 
   1.) Initalize a total vote counter equal to zero, delcare a list for candidates, dictionary for candiate votes, a county lsit, and county votes dictionary:
   
   ```py         
   total_votes= 0
   candidate_options = []
   candidate_votes ={}
   voting_counties = []
   county_votes = {}
   ```
   
   2.) Iterare through [Election Results](Resources/election_results.csv), get the candidate names, and begin to count the votes each time the name and county appears:
   
   ```py
   for row in reader:

        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]
        
        if candidate_name not in candidate_options:      
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
  
        if county_name not in voting_counties:
            voting_counties.append(county_name)    
            county_votes[county_name]=0
        county_votes[county_name]+= 1
    ```
* To finalize the total votes by county, percentage of vote by county, and determine the county with highest voter turnout:

   1.) Interate through the county_votes dictionary 
   
   ```py
   for county_name in county_votes:
     
        county_vote_count = county_votes[county_name]
        county_vote_percentage = float(county_vote_count)/ float(total_votes) * 100
        county_vote_results = (
            f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_vote_results)
    ```
   2.) Write a decison statement within the iteration to determine the winner:
   
   ```py
        if (county_vote_count > winning_county_count) and (county_vote_percentage > winning_percentage_county): 
            winning_county_count = county_vote_count
            winning_percentage_county = county_vote_percentage
            winning_county = county_name
     ```
     
Following a similar logic to that detailed above, the total number of votes by candiate, their repsective percentages, and the winner by popluar vote can be determined. Please see [PyPoll Code](PyPoll_Challenge.py) for completed code.


## Audit Summary

While this script is written specifcally for use in this congressional election, minor modifications can be made/added to apply this to any election or election data with more fields. A data field could be added to analyze the timing of votes (days of the week, hours of the day) to determine when people are voting and the staffing needed to handle the influx of voters. Also, the script could be applied to election data with demographics information to see the age groups, ethnicities, and genders of voters.
