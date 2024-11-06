#This was an assignment. 
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermon': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

# Iterate over the student_scores dictionary and assign grades
for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

#print(student_grades)  

#TODO: this is the final silent auction program code.


logo =''' 
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\                       
'''

print(logo)


def finding_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0 

    for bidder in bidding_dictionary: #bidder is the key i.e. the name of the bidder
        bid_amount = bidding_dictionary[bidder]  #this gives the value i.e. the bid price of the bidder.
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner}, with a bid of ${highest_bid}.") 


continue_bidding = True
Host_dictionary ={}

while continue_bidding:
    Name_input = input("What is your Name?")
    Bid_price = int(input("what is your Bid Price? $"))
    Host_dictionary[Name_input] = Bid_price
    Should_continue = input("Are there any other users who want bid? Type 'yes' or 'no'").lower()

    if Should_continue == "no":
        continue_bidding =False
        finding_highest_bidder(Host_dictionary)
    elif Should_continue == 'yes':
        print("\n" * 20) 

input("Press ENTER to exit!")
 
    #can use max() function along with .get method to get the max value 
    #of a key in Host_dictionary.
    #max_key = max(Host_dictionary, key=Host_dictionary.get)

#FIXME: or we can do the manual labor as well i.e. creating a user defined function. 
