#Main.py loads the ~\git\Python-Challenge\PyBank\Resources\budget_data.csv
#Created 11/16/2020 :Sushama Kunnath
import csv
import os
# Declare and Init
total_months=0
total_amount=0
diffRows=[]
months=[]
curr_row=0
prev_row=0
averageDiff=0
#Get the file path
csv_path=os.path.join('Resources', 'budget_data.csv')
csv_wpath=os.path.join('Analysis', 'PyBank.txt')

#Function to write the summary to file
def writeToFile(profitList):
    with open(csv_wpath, "w") as outfile:
        outfile.write("\n".join(str(i) for i in profitList))

#Open the budget_data file and read the contents
with open(csv_path) as csv_file :
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header= next(csv_reader)
    read_csv = list(csv_reader)

    #Added a counter to the iterable i   
    for i, row in enumerate(read_csv):
        #sum up the values from the file
        total_months=total_months+1
        total_amount=total_amount+int(row[1])
        #skip the first row since there is no previous value
        if i == 0:
            continue 
        #Subtract the current amount from the previous one and create lists
        curr_row=int(read_csv[i][1])
        prev_row=int(read_csv[i-1][1])
        diffRows.append(curr_row-prev_row)
        months.append(read_csv[i][0])
    # Average calculations, combining lists and getting the Min and Max from combined lists
    averageDiff=sum(diffRows)/len(diffRows)
    zipped=zip(months, diffRows)
    minProfit=min(zipped, key=lambda x : x[1])
    zipped=zip(months, diffRows)
    maxProfit=max(zipped, key=lambda x : x[1])
    

    #Write to file
    writeText=[]
    writeText.append(("Financial Analysis"))
    writeText.append("----------------------------")
    writeText.append("Total months : " + str(total_months))
    writeText.append("Total amount :" + "$" + str(total_amount))
    writeText.append(f"Average Change: ${averageDiff:.2f}")
    writeText.append(f"Greatest Increase in Profits: {str(maxProfit[0])} (${str(maxProfit[1])})")
    writeText.append(f"Greatest Decrease in Profits: {str(minProfit[0])} (${str(minProfit[1])})")
    writeToFile(writeText)
    
    #print the list output
    print(*(i for i in writeText), sep='\n')
    
