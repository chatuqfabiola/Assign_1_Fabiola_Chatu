import csv
revenue = {}

f = open("50000_Sales_Records.csv", 'rt')
reader = csv.reader(f)
next(reader)
#for row in reader:
#    print(row)

# step 3
# list of channels
sales_channels_list = ["offline", "online"]
print(sales_channels_list)

# Totals per sales channel (repeated for each sales channel)




# for row in reader:
#
#     if row[11] == "Total Revenue" and row[3] == "Offline":
#         Total_Revenue_count += 1
#         Total_Revenue += Decimal(row[11])
#
# print(f"Total revenue : {Total_Revenue_count}")

# dictionary= {}
for r in reader:
    total_revenue = r[11]

    if total_revenue in revenue:
        revenue[total_revenue] = revenue[total_revenue] + 1
    else:
        revenue[total_revenue] = 1

print(revenue)



