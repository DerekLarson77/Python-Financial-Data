# Python-Financial-Data

	There are two problem  in this challenge that are solved:  PyBank and PyPoll.  In both of them we are given a CSV file to put in a Resources folder.
An Analysis folder is created where the code will create a text document that will display our results as well.

PyBank:

	A function is created to receive inputs required to create write out each line to the text document within the analysis folder.

	Next a bunch of variables are declared to be equal to 0.  This was to avoid issues later within loops and if statements of variable not yet defined.

	A for loop is used to read through each row of the csv file.  Variables count various totals and there are if statements to check and save new greatest.

	Print statements are added to display in the console roughly the same layout as what is displayed in the instructions.

	The function is called with total_months, net_total, average_change, greatest_increase and greatest_decrease to create our text document.

PyPoll:

	A function to receive inputs required to create write out each line to the text document within the analysis folder.
		Within this function a for loop is used to write out the entire candidate list to their own row.  Hard coding was avoided in case there
		are a different number of candidates.

	A function to check if a name is already part of a candidate list.  If it's not on the list, it gets appended.

	Next a bunch of variables are declared to be equal to 0 and empty lists.  This was to avoid issues later within loops and if statements of variable or list not yet defined.
		The 4 list created are:
					csv_array:  Contents of the csv file
					candidates:  All unique candidates in csv file
					candidate_votes:  Total votes for each candidate
					votes_per:  Percentage of votes for each candidate

						In hindsight I would have created a Dictionary to save the last 3 lists and to ensure the votes and percentages
							easily aligned to the correct candidate.  

	A for loop is used to read through each row of the csv file.  Variables count various totals and there are if statements to check and save new greatest.
		csv_array saves each row of the csv file to a list.  This is to loop through csv_array again, because csv_reader will be at an index at the end of the csv 
		file and not loop through the file again.

	To remove all hard coding a nested for loop was created.  The outer loop goes through each candidate in our created candidate list.
		The inner loop goes through our created csv_array list that has the entire content of the csv file.
			If the candidate in the row matches the candidate of the outer loop matches a += was added to that candidates vote count value within candidate_votes list.
		After each inner loop is finished before going to the next candidate an if statement is used to check and save the current winner.
			The total candidate votes were divided by the total votes found in our original for loop to get the percentage of votes for that candidate
			and that is appended to the votes_per list for that candidate.

	Print statements are added to display in the console roughly the same layout as what is displayed in the instructions.
		A for loop is used to write out the entire candidate list to their own row.

	The function is called with total_votes, candidates, votes_per, candidate_votes, winner, vote_winner to create our text document.
