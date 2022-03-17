# Election Analysis

## Project Overview 
A Colorado Board of Elections employee has given you the following tasks to complete the eletion audit congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes and counties where it had a turnout.
3. Calculate the total number of votes each candidate received and turnout for each county. 
4. Calculate the percentage of votes each candidate won and county cast. 
5. Determine the winner of the election based on popular vote. 
6. Determine the county with the highest turnout. 
7. Calculate the percentage of votes each candidate won. 
8. Determine the winner of the elction based on the highest number of votes. 

## Resources 
- Data Srouce: election_results.csv 
- Software: Python 3.10.1, Visual Studio Code, 1.65.2

## Summary 
The analysis of the election show that: 
- There were "x" votes cast in the election. 
- The candidates were:                  - The counties were: 
    - Candidate 1                            - County 1 
    - Candidate 2                            - County 2 
    - Candidate 3                            - County 3                              
- The candidate results were: 
    - Candidate 1 receieved "x%" of the vote and "y" number of votes
    - Candidate 2 receieved "x%" of the vote and "y" number of votes.
    - Candidate 3 receieved "x%" of the vote and "y" number of votes.
 - The County results were: 
    - County 1 receieved "x%" of the vote and "y" number of votes
    - County 2 receieved "x%" of the vote and "y" number of votes.
    - County 3 receieved "x%" of the vote and "y" number of votes.
- The largest county turnout is: County (1, 2, or 3) where received the largest "x%" vote and "y" number of votes. 
- The winner of the election is: 
    - Candidate (1, 2, or 3), who receieved "x%" of the vote and "y" number of votes. 

## Election - Audit Results
- The total votes was 369,711 cotes in this congressional election. 
- The county results: 
    - Jefferson cast 10.5% of the vote & 38,855 votes.
    - Denver cast 82.8% of the vote & 306,055 votes.
    - Arapahoe cast 6.7% of the vote & 24,801 votes.
    - **Denever county had the largest turnout.**
- The candidate results: 
    - Charles Casper Stockham won 23.0% of the vote & 85,213 votes
    - Diana DeGette won 73.8% of the vote & 272,892 votes
    - Raymon Anthony Doane won 3.1% of the vote & 11,606 votes
    - **Diana DeGette won the election within 73.8% of the vote and 272,892 votes.** 

The output of the code is attached below. 
<img width="724" alt="Screen Shot 2022-03-14 at 2 34 27 AM" src="https://user-images.githubusercontent.com/83077836/158117670-9e298a90-be80-41f9-b399-caf80a897b86.png">

## Election - Audit Summary 
The program I have ran through is written to analyze the election_results.csv by iterating each row by using for loop. Also, by reading the data by list, starting from the second row and second & third column - County and Candidates - , we computed the number of votes for each county and candidate. By intialzing every variable into 0, (empty blank space for string type) I added the number of votes and accumulated as the program ran. Instead of counting all the data in csv file, we have inspected the data, read and wrote in order to ensure the result of the code. 



