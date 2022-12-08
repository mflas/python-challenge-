
#enable modules
import os
import csv
#set file path
budgetpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#Create new text file for outputing results
f = open("new_file.txt", "w")

mysum = []
with open(budgetpath) as budgetfile:
    csvreader = csv.reader(budgetfile,delimiter=',')
    print(csvreader)
    header = next (csvreader)   
    print (header)
    for row in csvreader:
#        print(int(row[1]))   
        mysum.append(int(row[1]))
    print("Total: $",sum(mysum))
    f.write("Total: $",sum(mysum))

a = mysum[-1]-mysum[0]
b = a//(len(mysum) - 1)
print("Average Change: $",b)
f.write("Average Change: $",b)

myset = set()
list2 = []
with open(budgetpath) as budgetfile:
    csvreader = csv.reader(budgetfile,delimiter=',')
    header = next (csvreader)   
    for row in csvreader:
        myset.add(row[0])
        list2.append(row[0])
    #print to screen
    print ("Total Months: ",len(myset))
    #write to file
    f.write("Total Months: ",len(myset))

print(list2)       
# mysum[0] - mysum[1]
list1 = []    

# find the month the greateest increase in profits
for i in range(len(mysum)-2):
    x=mysum[i+1] - mysum[i]
    list1.append(x)
    if mysum[i+1]- mysum[i] == max(list1):
        print(list2[i+1])
print("Greatest Increase in Profits: ",max(list1))
f.write("Greatest Increase in Profits: ",max(list1))

# find the month the greateest decrease in profits
list1 = []    
for i in range(len(mysum)-2):
    x=mysum[i] - mysum[i+1]
    list1.append(x)
    if max(list1)==mysum[i] - mysum[i+1]:
        print(list2[i+1])
print("Greatest Decrease in Profits: $-",max(list1))
f.write("Greatest Decrease in Profits: $-",max(list1))

#close file
f.close()
