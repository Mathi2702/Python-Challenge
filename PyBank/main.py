# Python script to analyze the financial records.
#To calculate the total number of months included in the dataset.
#The net total amount of "Profit/Losses" over the entire period and the average.
#To calculate the greatest increase and decrease in profits over the entire period.

#Import the os  and csv module to read the .csv file in the resources.
from datetime import date
import os
import csv
from statistics import mean

#defining variable
date = []
total_list = []
count_months =0
total_sum=0
change=0
change_list=[]
total_change=0
ave_change=0
max_change=0
min_change=0
min_change_date=0
max_change_date=0
pmonth=0

#file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#with function to read the csv file
with open(csvpath, 'r') as csvfile:

    #csv reader specifies the variable and delimiter
    csvreader=csv.reader(csvfile, delimiter=',')

    #To remove the header file
    header=next(csvreader)

    #for loop to read the .csv row by row
    for row in csvreader:
        date.append(row[0])
        total_list.append(row[1])
        count_months+=1
        total_sum+=int(row[1])
        #If statement to determine the change in "Profit/Losses"
        if pmonth!=0:
          change = int(row[1]) - int(pmonth)
          change_list.append(change)
          pmonth=row[1]
        else:
          pmonth=row[1]  
        #If statement to determine the greatest increase and decrease in profits  
        if change >max_change:
          max_change=change
          max_change_date=row[0]
        elif change<min_change:
          min_change=changecd
          min_change_date=row[0]  
            
    #To calculate the average of the changes
    ave_change=round(mean(change_list),2)

#print the below statements in the terminal
print('Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {count_months}\n'
    f'Total: ${total_sum}\n'
    f'Average Change: ${ave_change}\n'
    f'Greatest Increase in Profits: {max_change_date}(${max_change})\n'
    f'Greatest Decrease in Profits: {min_change_date}(${min_change})')

    
    
#defining path for output.textfile in Analysis folder
output=os.path.join('Analysis', 'output.txt')     
#to write the putput in the output.textfile         
with open(output, 'w') as textfile:
     textfile.write('Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {count_months}\n'
    f'Total: ${total_sum}\n'
    f'Average Change: ${ave_change}\n'
    f'Greatest Increase in Profits: {max_change_date}(${max_change})\n'
    f'Greatest Decrease in Profits: {min_change_date}(${min_change})')


