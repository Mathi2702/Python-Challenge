#PyPoll -Homework assignment
#Python script - To read the data from .csv file
#To calculate the total number of votes cast.
#A complete list of candidates who received votes.
#The total number of votes and percentage of their votes.
#The winner based on the popular vote
import os
import csv

#file path
csvpath = os.path.join('Resources', 'election_data.csv')

#defining variable
ballot_id = []
count = 0
candidate_list=[]
candidate_votes={}
votes=0
winner=0
winner_candidate=""

#with function to read the csv file
with open(csvpath, 'r') as csvfile:
    #csv reader specifies the variable and delimiter
    csvreader=csv.reader(csvfile, delimiter=',')

    #To remove the header file
    header=next(csvreader)

    #for loop to count the total id
    for row in csvreader:
        ballot_id.append(row[0])
        candidate_name = row[2]
        count += 1

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_list:
            #Add the candidate name to the candidate list.
            candidate_list.append(candidate_name)
            #Tracking the candidate's voter count.
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1
        else:
            #Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1    

#defining path for output.textfile in Analysis folder
output=os.path.join('Analysis', 'output.txt')   

#to write the output in the output.textfile 
with open(output, 'w') as textfile:   
    textfile.write('Election Results\n'
                '----------------------------------------\n'
                f'Total Vote:{count}\n'
                '----------------------------------------\n')              
    #for loop to calculate the percent
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        percent=float(votes/count)*100
        #if loop to determine the winner candidate with highest vote count
        if (votes>winner):
            winner=votes
            winner_candidate=candidate
        textfile.write(f"{candidate}: {percent:.3f}% ({votes:})\n")
                    

    textfile.write(f'----------------------------------------\n'
                   f'winner : {winner_candidate}\n'
                   f'----------------------------------------\n')            

#to write the output in the terminal 
print('Election Results\n'
                '----------------------------------------\n'
                f'Total Vote:{count}\n'
                '----------------------------------------\n')              
    #for loop to calculate the percent
for candidate in candidate_votes:
    votes=candidate_votes[candidate]
    percent=float(votes/count)*100
    #if loop to determine the winner candidate with highest vote count
    if (votes>winner):
        winner=votes
        winner_candidate=candidate
    print(f"{candidate}: {percent:.3f}% ({votes:})\n")
print(f'----------------------------------------\n'
      f'winner : {winner_candidate}\n'
      f'----------------------------------------\n')        
     