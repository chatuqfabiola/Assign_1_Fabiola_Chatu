import csv

revenue = []
s = set()

f = open("50000_Sales_Records.csv", 'rt')
reader = csv.reader(f)
next(reader)
#for row in reader:
#    print(row)

#The average revenue of all the units sold for channel.
# c. The total revenue for channel.


# build the sets, question 1: A list of sales channels
# 'Online', 'Offline'

for r in reader:

    revenue.append(r[11])
    total_revenue = r[11]
    s.add(total_revenue)

print(s)
sales_channels_list = ["offline", "online"]

