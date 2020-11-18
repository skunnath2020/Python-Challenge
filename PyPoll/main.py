#Main.py loads the ~\git\Python-Challenge\PyPoll\Resources\election_data.csv
#Created 11/18/2020 :Sushama Kunnath
import csv
import os
# Declare and Init
total_votes=0
average=0 
set_values=[]


#Get the file path
csv_path=os.path.join('Resources', "election_data.csv")
csv_wpath=os.path.join('Analysis', "PyPoll.txt")

#Summary to file
def writeToFile(pollList):
    with open(csv_wpath, "w") as outfile:
        outfile.write("\n".join(str(i) for i in pollList))

# Open the data file and read the contents
with open(csv_path) as csv_file :
    csv_reader = csv.reader(csv_file, delimiter=',')
    #skip the header
    csv_header=next(csv_reader)
    read_csv = list(csv_reader)

    # Get the list of candidates from the last row
    candidates=[row[2] for row in read_csv]
    uniq_candidates=set(candidates)
   
    # Get the total votes
    total_votes= len([votes for votes in read_csv])
    
    # Store the unique candidates as key in dictionary voter_summary
    voter_summary={key:[] for key in uniq_candidates}
    # Calculate votes, average for each candidate and store in the form {key: [val1, val2]}
    # where key is the candidate name
    for key, val in voter_summary.items():
        # for each key in dictionary count the total votes from read_csv
        votes=len([i for i in read_csv if i[2]==key])
        average=(votes/total_votes) *100
        # insert the list to the dictionary
        voter_summary[key].append(average)
        voter_summary[key].append(votes)
# Sort the dictionary by the the list value:average    
sorted_votes=dict()
# the key here refers to the sort key which is the second element in the dictionary
sorted_votes={k: v for k, v in sorted(voter_summary.items(), key=lambda item: item[1], reverse=True)}

# Write to file
writeText=[]      
writeText.append(("Election Results")) 
writeText.append(("-------------------------------"))
writeText.append((f"Total votes: {total_votes}"))    
writeText.append(("-------------------------------"))
# print dictionary for key, val
for key, value in sorted_votes.items():
    writeText.append((f"{key}: {round(value[0]):.3f}%  ({value[1]})"))
writeText.append(("-------------------------------"))
writeText.append((f"Winner: {list(sorted_votes.keys())[0]} "))    
writeText.append(("-------------------------------"))
writeToFile(writeText)
# print the list output
print(*(i for i in writeText), sep='\n')