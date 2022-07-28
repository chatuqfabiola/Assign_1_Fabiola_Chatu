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

