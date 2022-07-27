import csv
# 1. build the sets, question 1: A list of sales channels

records = []
sales = set()
offline_count = 0
online_count = 0


f = open("50000_Sales_Records.csv", 'rt')
reader = csv.reader(f)
next(reader)
#for row in reader:
 #   print(row)


for r in reader:

    records.append(r[3])

    sales_channel = r[3]
    sales.add(sales_channel)

print(sales)


# Q2: Totals per sales channel (repeated for each sales channel).
length = len(sales)
print(length)

# Go to each ; Total for offline and total online

for regions in sales:

    print(f"Total for {regions}")





