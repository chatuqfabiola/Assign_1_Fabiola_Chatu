import csv
from decimal import Decimal

revenue_count = 0
total_revenue = 0

# 3. Big totals
# a_ The number of total units sold.
# b. The average revenue of all the units sold.
# c. The total revenue.

f = open("50000_Sales_Records.csv", 'rt')
reader = csv.reader(f)
next(reader)
#for row in reader:
#    print(row)

for r in reader:

    if r[11] != "":
        revenue_count += 1
        total_revenue += Decimal(r[11])

average_revenue = total_revenue / revenue_count


print(f"The number of total units sold is : {revenue_count}")
print(f"The average revenue of all the units sold is : {average_revenue}")
print(f"The total revenue is : {total_revenue}")

