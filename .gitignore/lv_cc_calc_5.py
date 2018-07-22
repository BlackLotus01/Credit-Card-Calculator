cards = ["card 1", "card 2", "card 3"]
spend_categories = ["Airfaire", "Hotel", "Travel(other)", "Reaurants", "Gas", "Groceries", "Other"]


total_credits_list = []
total_fees_list = []
spend_points_list = []
point_value_list = []
bonus_points_list = []
expected_value_list = []


        
def get_cards():
    total = 0
    i = 0
    while total < len(cards):
        cards[i] = input("What is the name of " + cards[i] + "?" )
        total += 1
        i += 1
    return


#calculates that amount of annual credits.
def total_credits():
    i = 0
    while len(total_credits_list) < len(cards):
        travel_credit = int(input("What is the annual travel credit for the " + cards[i] + " card?" ))
#        ride_credit = int(input("How much in ride sharing credit do you expect to receive for "  + cards[0] + "?"))
#        hotel_credit = int(input("How much in hotel credit do you expect to receive for " + cards[0] + "?"))
#        shopping_credit = int(input("How much in shopping_credit do you expect to receive for " + cards[0] + "?"))
#        other_credit = int(input("How much in other credits do you expect to receive for " + cards[0] + "?"))
        total_credits = travel_credit #+ ride_credit + hotel_credit + shopping_credit + other_credit
        total_credits_list.append(total_credits)
        print("You will receive " + str(total_credits) + " dollars in total credits for the " + cards[i] + " card.")
        print('')
        i += 1
    return


#Get the amount you expect to pay in fee per year.
def total_fees():
    i = 0
    while len(total_fees_list) < len(cards):
        annual_fee = int(input("What is the annual fee for " + cards[i] + "?" ))
#        authorized_users = int(input("What is the total authorized user fee for " + cards[0] + "?" ))
#        foriegn_fee = int(input("How much do you expect to pay in foriegn transaction fees for " + cards[0] + "?" ))
#        other_fees = int(input("How much are all other fees for " + cards[0] + "?" ))
        total_fees = annual_fee #+ authorized_users + foriegn_fee + other_fees
        total_fees_list.append(total_fees)
        print("You will pay " + str(total_fees) + " dollars in total fees for the " + cards[i] + " card.")
        print('')
        i += 1
    return  


#This needs to be broken down into other categories.
#For now a card holder will just have to apporximate the amount of points he/she will earn in a given year.
def spend_points():
    i = 0
    while len(spend_points_list) < len(cards):
        spend_points = int(input("How many points do you expect to receive from everyday spend for the " + cards[i] + " card?" ))
        spend_points_list.append(spend_points)
        print("You expect to earn " + str(spend_points) + " points for regular spend on the " + cards[i] + " card.")
        print('')
        i += 1
    return

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

def bonus_points():
    i = 0
    while len(bonus_points_list) < len(cards):
        bonus_points = str(input("Will you be receiving a sign up bonus for the " + cards[i] + " card?"))
        if bonus_points == "yes":
            bonus_points = int(input("How many bonus points will you recieve for the " + cards[i] + " card?" ))
        else:
            bonus_points = 0
        bonus_points_list.append(bonus_points)
        i += 1
    return

def expected_value():
    i = 0
    while len(expected_value_list) < len(cards):
        expected_value = (total_credits_list[i] - total_fees_list[i] +
                          (spend_points_list[i] * point_value_list[i]) +
                          (bonus_points_list[i] * point_value_list[i]))
        expected_value_list.append(expected_value)
        print("The expected value for the " + cards[i] + " card is " + str(expected_value) + " dollars.")
        print('')
        i += 1
    return


get_cards()
total_credits()
total_fees()
spend_points()
point_value()
bonus_points()
print('')
expected_value()

