import os
import csv

budgetpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(budgetpath) as budgetfile:
    csvreader = csv.reader(budgetfile,delimiter=',')
    print(csvreader)
    header = next (csvreader)   
    print (header)
    for row in csvreader:
        print(row)