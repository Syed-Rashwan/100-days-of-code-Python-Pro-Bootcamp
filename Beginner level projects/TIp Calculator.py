
bill =float(input("How much was the bill $?"))

tip = int(input("How much would you like to tip? 10 15 20 "))

people = int(input("How many people to split the bill?"))

total_bill = bill + tip

bill_per_person = total_bill / people

final_amount = round(bill_per_person)

print(f"Each person should pay ${final_amount}")

input('Press ENTER to exit!')