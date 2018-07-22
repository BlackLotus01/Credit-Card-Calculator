cards = ["card 1", "card 2", "card 3"]


total_credits_list = []
total_fees_list = []
spend_points_list = []
point_value_list = []
expected_value_list = []
sign_up_bonus_list = []


#main program
def best_option():
    total = 0
    i = 0
    while total < len(cards):
        cards[i] = input("What is the name of " + cards[i] + "?" )
        total += 1
        i += 1
    total = 0
    i = 0
    while total < len(cards):
        totalCredit = get_total_credits()
        total_credits_list.append(totalCredit)
        print("You will receive " + str(totalCredit) + " dollars in total credits for the " + cards[i] + " card.")
        print('')
        total += 1
        i +=1
    total = 0
    i = 0
    while total < len(cards):
        totalFees = get_total_fees()
        total_fees_list.append(totalFees)
        print("You will pay " + str(totalFees) + " dollars in total fees for the " + cards[i] + " card.")
        print('')
        total += 1
        i +=1
    total = 0
    i = 0
    while total < len(cards):
        spendPoints = spend_points()
        spend_points_list.append(spendPoints)
        print("You expect to earn", spendPoints, "points per year.")
        print('')
        total += 1
        i += 1
    total = 0
    i = 0
    point_value()
    bonus_points
    while total < len(cards):
        expected_value = (total_credits_list[i] - total_fees_list[i] + 
                         (spend_points_list[i] * point_value_list[i]) + 
                         (bonusPoints * point_value_list[i]))
        expected_value_list.append(expect_value)
        total += 1
        i += 1

        



#calculates that amount of annual credits.
def get_total_credits():
    if len(total_credits_list) == 0:
        travel_credit = int(input("What is the annual travel credit for " + cards[0] + "?" ))
#        ride_credit = int(input("How much in ride sharing credit do you expect to receive for "  + cards[0] + "?"))
#        hotel_credit = int(input("How much in hotel credit do you expect to receive for " + cards[0] + "?"))
#        shopping_credit = int(input("How much in shopping_credit do you expect to receive for " + cards[0] + "?"))
#        other_credit = int(input("How much in other credits do you expect to receive for " + cards[0] + "?"))
    elif len(total_credits_list) == 1:
        travel_credit = int(input("What is the annual travel credit for " + cards[1] + "?" ))
#        ride_credit = int(input("How much in ride sharing credit do you expect to receive for " + cards[1] + "?"))
#        hotel_credit = int(input("How much in hotel credit do you expect to receive for " + cards[1] + "?"))
#        shopping_credit = int(input("How much in shopping_credit do you expect to receive for " + cards[1] + "?"))
#        other_credit = int(input("How much in other credits do you expect to receive for " + cards[1] + "?"))
    else:
        travel_credit = int(input("What is the annual travel credit for " + cards[2] + "?" ))
#        ride_credit = int(input("How much in ride sharing credit do you expect to receive for " + cards[2] + "?"))
#        hotel_credit = int(input("How much in hotel credit do you expect to receive for " + cards[2] + "?"))
#        shopping_credit = int(input("How much in shopping_credit do you expect to receive for " + cards[2] + "?"))
#        other_credit = int(input("How much in other credits do you expect to receive for " + cards[2] + "?"))
    get_total_credits = travel_credit #+ ride_credit + hotel_credit + shopping_credit + other_credit
    print('')
    return get_total_credits


#Get the amount you expect to pay in fee per year.
def get_total_fees():
    if len(total_fees_list) == 0:
        annual_fee = int(input("What is the annual fee for " + cards[0] + "?" ))
#        authorized_users = int(input("What is the total authorized user fee for " + cards[0] + "?" ))
#        foriegn_fee = int(input("How much do you expect to pay in foriegn transaction fees for " + cards[0] + "?" ))
#        other_fees = int(input("How much are all other fees for " + cards[0] + "?" ))
    elif len(total_fees_list) == 1:
        annual_fee = int(input("What is the annual fee for " + cards[1] + "?" ))
#        authorized_users = int(input("What is the total authorized user fee for " + cards[1] + "" ))
#        foriegn_fee = int(input("How much do you expect to pay in foriegn transaction fees for " + cards[1] + "?" ))
#        other_fees = int(input("How much are all other fees for " + cards[1] + "?" ))
    else:
        annual_fee = int(input("What is the annual fee for " + cards[2] + "?" ))
#        authorized_users = int(input("What is the total authorized user fee for " + cards[2] + "?" ))
#        foriegn_fee = int(input("How much do you expect to pay in foriegn transaction fees for " + cards[2] + "?" ))
#        other_fees = int(input("How much are all other fees for " + cards[2] + "?" ))
    get_total_fees = annual_fee #+ authorized_users + foriegn_fee + other_fees
    print('')
    return get_total_fees 


#This needs to be broken down into other categories.
#For now a card holder will just have to apporximate the amount of points he/she will earn in a given year.
def spend_points():
    if len(spend_points_list) == 0:
        spend_points = int(input("How many points do you expect to receive from everyday spend for the " + cards[0] + " card?" ))
    elif len(spend_points_list) == 1:
        spend_points = int(input("How many points do you expect to receive from everyday spend for the " + cards[1] + " card?" ))
    else:
        spend_points = int(input("How many points do you expect to receive from everyday spend for the " + cards[2] + " card?" ))
    return spend_points

def point_value():
    i = 0
    while len(point_value_list) < len(cards):
        point_value = float(input("In terms of cents per point, how much do you value the points for the " + cards[i] + " card."))
        point_value = point_value / 100
        point_value_list.append(point_value)
        print("You place a value of " + str(point_value) + " per point for the " + cards[i] +".")
        print('')
        i += 1
    return

def sign_up_bonus():
    i = 0
    while len(sign_up_bonus_list) < len(cards):
        receive_bonus = str(input("Will you be receiving a sign up bonus for the " + cards[i] + " card?"))
    if receive_bonus == "yes":
        sign_up_bonus = int(input("How many bonus points will you recieve for the " + cards[i] + " card?" ))
    else:
        sign_up_bonus = 0
        sign_up_bonus_list.append(sign_up_bonus)
    return

best_option()
