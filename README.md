# Assign_1_Fabiola_Chatu


Program #1 – Tip Calculator


FEDERAL_TAX = 0.05
PROVINCIAL_TAX = 0.09775
Horrible = int(4)
Basic = int(3)
Good = int(2)
Exceptional = int(1)

num_diners = int(input("How many diners are? "))
meal_before_tax = int(input(" What is the cost of every meal before taxes? "))
amount_tip = int(input(" How much do you want to tip? Chose 1 , 2 , 3 or 4 : "
                       "'4-Horrible(0%)', '3-Basic(10%)', '2-Good(15%)', '1-Exceptional(20%)' "))

#If the user chooses 2, then the tip percentage is 15%

if amount_tip == int(2):
    print("the service was Good, tip percentage is 15% " + "Thanks")

elif amount_tip == int(3):
    print ("the service was Basic tip percentage is 10% ")

elif amount_tip == int(1):
    print ("the service was Exceptional, tip percentage is 20% ")

elif amount_tip == int(4):
    print ("the service was Horrible, tip percentage is 10% ")

else:

    print("The value is not correct, the program will restart")

exit()


meal_fed_tax = (meal_before_tax * FEDERAL_TAX) + meal_before_tax
meal_prov_tax = (meal_before_tax * PROVINCIAL_TAX) + meal_before_tax
total_meal_price = (meal_before_tax * FEDERAL_TAX) + (meal_before_tax * PROVINCIAL_TAX) + meal_before_tax

tip_based_price_before_tax = (meal_before_tax * amount_tip) + meal_before_tax

grand_total_including_tax = total_meal_price + tip_based_price_before_tax
amount_owed_per_person = grand_total_including_tax / num_diners


print(num_diners)
print(meal_before_tax)
print(amount_tip)
print(meal_prov_tax)
print(meal_fed_tax)
print(total_meal_price)
print(tip_based_price_before_tax)
print(grand_total_including_tax)
print(amount_owed_per_person)

# PROJET 2 

import csv
# 1. build the sets, question 1: A list of sales channels

records = []
sales = set()
regions = []
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

import csv

f = open("50000_Sales_Records.csv", 'rt')
reader = csv.reader(f)
next(reader)
#for row in reader:
#    print(row)

sales = set()
regions = []
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


# Go to each ; Total for offline and total online

for regions in sales:

    print(f"Total for {regions}")


# QUESTION 3

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


# QUESTION 2: AVERAGE FOR REGIONS (OFFLINE AND ONLINE)

import csv
from decimal import Decimal

offline_count = 0
online_count = 0
revenue_count = 0
offline_total_revenue = Decimal(0.00)
online_total_revenue = Decimal(0.00)
total_revenue = 0

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


# QUESTION 4: THE TOTAL REVENUE

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




# THE END






