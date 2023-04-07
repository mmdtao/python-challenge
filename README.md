# python-challenge
## Overview of Project

### Purpose
The purpose of the Python Challenges were to use Python to first analyze a series of bank profits to show the total profit, average change, min and max profits over the course of 86 months. The second challenge required analyzing an election to show the candidates who participated and their respective vote counts and percentages.

## Analysis and Challenges
### PyBank
In the PyBank challenge, the main challenge was developing the for loop script to run through our budget_data csv file and create lists which could then be analyzed mathmatically. Logically, the loop needed to track the total months and its respective date in a list before performing calculations as shown below:
<img width="602" alt="Screenshot 2023-04-06 at 10 53 05 PM" src="https://user-images.githubusercontent.com/114324871/230537616-b036ae6e-6128-4b2a-be5a-0a611f26f785.png">

The challenge for this particular code was that my monthly_changes list included the initial profit and while I did not find a particularly clean solution, I was able to sum the list excluding the first value and subtracting a month from total_months. This is reflected in the script for the printing portion of my code:
<img width="889" alt="Screenshot 2023-04-06 at 10 56 41 PM" src="https://user-images.githubusercontent.com/114324871/230538054-ee0590d4-54e2-42de-b1a8-467f2d17c939.png">

### PyPoll
In the PyPoll challenge, I separated the analysis using two for loops. The first loop reads the csv file and identifies the candidates, storing them into a list called candidate_options and counts each candidate's votes and stores them in a candidate_votes list (shown below). 
<img width="386" alt="Screenshot 2023-04-06 at 11 02 39 PM" src="https://user-images.githubusercontent.com/114324871/230538602-c36a00dd-6a15-4d9b-988a-f455048d3523.png">


The second for loop calculates each candidate's vote percentage and prints the results and writes a text file (shown below)
<img width="562" alt="Screenshot 2023-04-06 at 11 03 40 PM" src="https://user-images.githubusercontent.com/114324871/230538680-146da012-fdef-4c0e-89fd-d8ec4152e062.png">


