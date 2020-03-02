#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import os
import csv


# In[2]:


# Establish filepath
budget_csv = os.path.join(".", "resources", "budget_data.csv")
output_file = os.path.join(".", "financial_analysis.txt")


# In[3]:


# Index Reference for the Profit and Loss List

# Track Financial Parameters

# Open and read csv file
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Captures and removes the header row (list) into csvheader
    csvheader = next(csvreader) 
    
    # Set up Counter, had to circle back to adjust bc of using next(csvreader) twice
    total_months = 0
    total_months = total_months + 1
    
    # Setup for change analysis and calculations
    financial_data = [867884]
    
    # Calculating the "Average of Changes" and Tracking the Month
    netchange_list = []
    month_of_change_list = []
    
    # Greatest Increase / Decrease- use list, save spot for Period and Value
    # counter intuitive
    greatest_increase = ["", 0]
    greatest_decrease = ["", 999999]
    
    # Captures and removes the next row into first_row (Python knows to go to the next line / list down in the csvreader)
    first_row = next(csvreader) # first whole row is a list month & value
    
    # Isolate the first value of "Profit/Losses"
    # Note: the first_row[0] is Jan-10
    prev_net = int(first_row[1])
    
    for row in csvreader:
        #print(f"{row[0]} , {row[1]}")
        
        # Loop Thru and count the total number of months included in the dataset
        total_months += 1
        
        # The net total amount of “Profit/Losses” over the entire period
        financial_data.append(int(row[1]))
        
        # Average of the changes in “Profit/Losses” over the entire period
        #Part one: "Numberator" Net Change
        
        # Track the net change
        # This calculates Month to Month (differences) aka changes
        net_change = int(row[1]) - int(prev_net) # @ this point prev_net = first value
        # This appends those changes to the list
        netchange_list.append(net_change) #- JG initial thought
        prev_net = int(row[1])
        #netchange_list.append(net_change) # solution. test after
        
        # Track month of change as well
        #month_of_change_list = month_of_change_list + [row[0]] # concatenate row[0] to the list
        month_of_change_list.append(row[0]) # add the month of change to list
        # will not need this for calculations
    
        # Greatest increase and decrease in the dataset caculations
        
        if net_change > greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = row[0] #capture the month
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = row[0]
    
    
    net = sum(financial_data)
    
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net}\n"
    f"Average Change: {sum(netchange_list)/len(netchange_list)}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} '({greatest_increase[1]})'\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} '({greatest_decrease[1]})'\n"
    )

with open ("financial_analysis.txt", 'w') as txt_file:
    txt_file.write(output)


# In[ ]:


# Test Cells

with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) 
    
    total_months = 0
    financial_data = []
    rolling_average = []
    
    first_row = next(csvreader)
    
    print(first_row[1])


# In[ ]:


# test cells below.


# In[ ]:


(first_row[1])


# In[ ]:


csvheader


# In[ ]:


type(greatest_increase[1])


# In[ ]:




