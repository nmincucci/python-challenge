#Import modules
import os
import csv
import pandas as pd

#Define the path to the input CSV file
csvpath = os.path.join("C:/Users/Nick/PythonChallenge/python-challenge/PyBank/budget_data.csv")

#Open the input CSV file                       
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #Read the CSV file
    print(csvreader)

    #Read and print CSV header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
                    
#Read the CSV file into a DataFrame
df = pd.read_csv(csvpath)

#Calculates number of rows in CSV file (Months)
num_rows = len(df) 

#Calculate the total sum of 'Profit/Losses' column
column_to_sum = 'Profit/Losses'
column_sum = df[column_to_sum].sum()

#Calculate the average change in 'Profit/Losses'
df['Profit/Losses Change'] = df['Profit/Losses'].diff()
avg_change = df['Profit/Losses Change'].mean()

#Find the row with greatest increase in profits
df['Difference'] = df[column_to_sum].diff()
greatest_increase_row = df.loc[df['Difference'].idxmax()]
increase_date = greatest_increase_row['Date']
increase_amount = greatest_increase_row['Difference']

#Find the row with greatest decrease in profits
greatest_decrease_row = df.loc[df['Difference'].idxmin()]
decrease_date = greatest_decrease_row['Date']
decrease_amount = greatest_decrease_row['Difference']

# Print the financial analysis results to the terminal
print("Financial Analysis")
print("------------------")
print("Total months:", num_rows)
print(f"Total: ${column_sum}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Decrease in Profits: {increase_date} (${increase_amount})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_amount})")

# Export the financial analysis results to a text file
with open('financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {num_rows}\n")
    file.write(f"Total Profit/Losses: ${column_sum}\n")
    file.write(f"Average Change: (${avg_change:.2f})\n")
    file.write(f"Greatest Increase in Profits: {increase_date} (${increase_amount:.0f})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease_amount:.0f})\n")

#Tell user about creation of text file
print("Analysis results have been exported to 'financial_analysis.txt'")
