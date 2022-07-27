import csv


f = open("50000_Sales_Records.csv", 'rt')
reader = csv.reader(f)
next(reader)
#for row in reader:
#    print(row)

offline_count = 0
online_count = 0
not_responded = 0


# Q2.a. The number of total units sold for channel.

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
