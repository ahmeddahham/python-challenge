# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

import os

print("Financial Analysis")
print("-------------------")
csvpath=os.path.join('Resources','budget_data.csv')
with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
    lines = lines.split("\n")
    profits =[]
    Months =[]
    Change =[]
    for row in range(1,len(lines)-1) :
        Temp = lines[row].split(',')
        profits.append(int(Temp [1]))
        Months.append(Temp[0])

    print("Total_month: "+str(len(Months)))
    print("Total: $" + str(sum(profits)))

    for x in range(1,len(profits)):
        Change.append(profits[x]-profits[x-1])
    Average=sum(Change)/len(Change)
    print("Average Change : $"+str(round(Average,2)))
    Increase_number =max(Change)
    print("Greatest increase in profits: " +Months[Change.index(Increase_number)+1] + " $"+ str(Increase_number))
    Greatest_Decrease =min(Change)
    print("Greatest Decrease in profits: " + Months[Change.index( Greatest_Decrease) + 1] + " $" + str( Greatest_Decrease))

    analysis_path=os.path.join('analysis')
    os.chdir(analysis_path)
    f = open("analysis.txt", "w")
    f.write("Financial Analysis")
    f.write("\n-------------------")
    f.write("\nTotal_month: "+str(len(Months)))
    f.write ("\nTotal: $" + str(sum(profits)))
    f.write("\nAverage Change : $"+str(round(Average,2)))
    f.write("\nGreatest increase in profits: " +Months[Change.index(Increase_number)+1] + " $"+ str(Increase_number))
    f.write("\nGreatest Decrease in profits: " + Months[Change.index( Greatest_Decrease) + 1] + " $" + str( Greatest_Decrease))


    f.close()
    file_handler.close()



