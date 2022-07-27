import csv
from decimal import Decimal

offline_count = 0
online_count = 0
revenue_count = 0
offline_total_revenue = Decimal(0.00)
online_total_revenue = Decimal(0.00)

#The average revenue of all the units sold for channel.
# c. The total revenue for channel.

f = open("50000_Sales_Records.csv", 'rt')
reader = csv.reader(f)
next(reader)
#for row in reader:
#    print(row)

for row in reader:

    if row[3] == "Offline" and "total_revenue" == Decimal(row[11]):
        print(f"total revenue for channel Offline is : {offline_total_revenue}")


    else row[3] == "Online" and "total_revenue" == Decimal(row[11]):
        print(f"total revenue for channel Online is : {online_total_revenue}")


        online_count += 1
        revenue_count += 1
        total_revenue += Decimal(row[11])

print(f"total revenue for channel Offline is : {offline_count}")
print(f"total revenue for channel Online is: {online_count}")
print(revenue_count)
print(total_revenue)

print("Total revenue of " + str(CHECK_MULTIPLE) + ".")
offline_count += 1
revenue_count += 1