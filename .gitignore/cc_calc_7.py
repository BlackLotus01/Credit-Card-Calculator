#This calculator assumes U.S. dollars for all currency portions.

cards = ["card 1", "card 2", "card 3"]
categories = ["airfaire", "hotels", "other travel", "restaurants", "Gas", "Groceries", "other items/services"]

categories_spend_list = []
total_credits_list = []
total_fees_list = []
spend_points_list = []
point_value_list = []
bonus_points_list = []
expected_value_list = []




                               
# Replace the placeholders in the card list with the name of the cards the user wants to compare.
def get_cards():
    total = 0
    i = 0
    while total < len(cards):
        cards[i] = input("What is the name of " + cards[i] + "? ")
        total += 1
        i += 1
    return


#Calculates the amount of annual credits for each card.
def total_credits():
    i = 0
    while len(total_credits_list) < len(cards):
        travel_credit = int(input("What is the annual travel credit for the " + cards[i] + " card? "))
        ride_credit = int(input("How much in ride sharing credit do you expect to receive for "  + cards[i] + "? "))
        hotel_credit = int(input("How much in hotel credit do you expect to receive for " + cards[i] + "? "))
        shopping_credit = int(input("How much in shopping_credit do you expect to receive for " + cards[i] + "? "))
        other_credit = int(input("How much in other credits do you expect to receive for " + cards[i] + "? "))
        total_credits = travel_credit + ride_credit + hotel_credit + shopping_credit + other_credit
        total_credits_list.append(total_credits)
        print("You will receive " + str(total_credits) + " dollars in total credits for the " + cards[i] + " card.")
        print('')
        i += 1
    return


#Calculates the amount you expect to pay in fees per year per card.
def total_fees():
    i = 0
    while len(total_fees_list) < len(cards):
        annual_fee = int(input("What is the annual fee for " + cards[i] + "? "))
        authorized_users = int(input("What is the total authorized user fee for " + cards[i] + "? "))
        foriegn_fee = int(input("How much do you expect to pay in foriegn transaction fees for " + cards[i] + "? "))
        other_fees = int(input("How much are all other fees for " + cards[i] + "? "))
        total_fees = annual_fee + authorized_users + foriegn_fee + other_fees
        total_fees_list.append(total_fees)
        print("You will pay " + str(total_fees) + " dollars in total fees for the " + cards[i] + " card.")
        print('')
        i += 1
    return  

#Spend points calculates the number of points a user expects to earn based on the credit cards categories and spending multipliers.
def spend_points():
    categories_spend()
    print('')
    multiplier()

#This totals the amound a user expects to spend for each of the predefined spending categories.
#The total for categories_spend will be applied to all cards in the cards list.
def categories_spend():
    i = 0
    while len(categories_spend_list) < len(categories):
        if i < len(categories):
            categories_spend = int(input("How much do you expect to spend on " + categories[i] + "."))
            categories_spend_list.append(categories_spend)
            i += 1
    return

#This applies the appropriate multiplier for each spend amount in the categories_spend_list, for each card.
def multiplier():
    spend_points_temp = 0
    i = 0
    j = 0
    while len(spend_points_list) < len(cards):
        if i < len(categories):
            multiplier_temp = float(input("How many points per dollar will you earn on " + categories[i] + " for the " + cards[j] + " card."))
            print('')
            spend_points_temp += (categories_spend_list[i] * multiplier_temp)
            i += 1
        else:
            spend_points_list.append(spend_points_temp)
            print('')
            print("You expect to earn " + str(spend_points_temp) + "points for regular spend on the " + cards[j] + " card.")
            print('')
            i = 0
            j += 1
            spend_points_temp = 0
    return

#This places the value, in US dollars, the user places for each the points of each card.
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

#This takes into consideration if the user will earn bonus points for the first year of possessing a card.
def bonus_points():
    i = 0
    while len(bonus_points_list) < len(cards):
        bonus_points = str(input("Will you be receiving a sign up bonus for the " + cards[i] + " card? "))
        if bonus_points == "yes" or "Yes" or "YES":
            bonus_points = int(input("How many bonus points will you recieve for the " + cards[i] + " card? " ))
        else:
            bonus_points = 0
        bonus_points_list.append(bonus_points)
        i += 1
    return

#This performs the final calculation.
def expected_value():
    i = 0
    while len(expected_value_list) < len(cards):
        expected_value = (total_credits_list[i] - total_fees_list[i] +
                          (spend_points_list[i] * point_value_list[i]) +
                          (bonus_points_list[i] * point_value_list[i]))
        expected_value_list.append(expected_value)
        print("The expected value for the " + cards[i] + " card, is " + str(expected_value) + " dollars.")
        print('')
        i += 1
    return


#The main credit card calculation program.
def ccCalc():
    get_cards()
    print('')
    total_credits()
    print('')
    total_fees()
    print('')
    spend_points()
    print('')
    point_value()
    print('')
    bonus_points()
    print('')
    expected_value()

    
    maxev = max(expected_value_list)
    maxPosition = expected_value_list.index(maxev)
    maxevCount = expected_value_list.count(maxev)

    #ev = expected value; idx = index
    if maxevCount == 1:
            print("The", cards[maxPosition], "card provides you the best value, with an expected value of", str(maxev) + ".")
    else:
            for idx, ev in enumerate(expected_value_list):
                    if ev == maxev:
                            print("The", cards[idx], "is one of the cards that will provide you the best value, with an expected value of", str(maxev) + ".")


if __name__ == '__main__':
    ccCalc()
