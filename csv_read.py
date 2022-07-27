import csv
from decimal import Decimal

offline_count = 0
online_count = 0
not_responded = 0
Total_Revenue = Decimal(0.00)
Total_Revenue_count = 0
unit_sold_count = 0

f = open("50000_Sales_Records.csv", 'rt')
reader = csv.reader(f)
next(reader)
#for row in reader:
#    print(row)

# step 3
# 1. list of channels

sales_channels_list = ["offline", "online"]
print(sales_channels_list)

# 2. Totals per sales channel (repeated for each sales channel)

for row in reader:

    if row[3] == "Offline":
        offline_count += 1
    elif row[3] == "Online":
        online_count += 1
    elif row[3] == "":
        not_responded += 1

print(f"Number of total units Offline is : {offline_count}")
print(f"Number of total units Online is: {online_count}")
print(f"Number of non_responded is: {not_responded}")

# 4.The total revenue for channel
# 3. average revenue of all the units sold for channel.

for row in reader:

    if row[11] == "Total Revenue":
        Total_Revenue_count += 1
        Total_Revenue += Decimal(row[11])

#average_revenue = Total_Revenue / Total_Revenue_count
#print(f"Average revenue is : ${average_revenue}")

print(Total_Revenue_count)
print(Total_Revenue)
print(f"The total revenue is : {Total_Revenue}")

# 3. Big totals
#a. The number of total units sold.





#b. The average revenue of all the units sold.
#c. The total revenue.

