

#Get the total amount in credit a user will receive per year.
def total_credits():
    total_credits = 0
    travel_credit = int(input("What is the annual travel credit?" ))
    ride_credit = int(input("How much in ride sharing credit do you expect to receive?" ))
    hotel_credit = int(input("How much in hotel credit do you expect to receive?" ))
    shopping_credit = int(input("How much in shopping_credit do you expect to receive?" ))
    other_credit = int(input("How much do you expect to receive for other credits?" ))
    total_credits = travel_credit + ride_credit + hotel_credit + shopping_credit + other_credit
    print("You will receive", str(total_credits), "dollars in total credits.")
    return total_credits

#Get the amount you expect to pay in fee per year.
def total_fees():
    total_fees = 0
    annual_fee = int(input("What is the annual fee?" ))
    authorized_users = int(input("What is the total authorized user fee?" ))
    foriegn_fee = int(input("How much do you expect to pay in foriegn transaction fees?" ))
    other_fees = int(input("How much were you charged for all other fees?" ))
    total_fees = annual_fee + authorized_users + foriegn_fee + other_fees
    print("You will pay", str(total_fees), "dollars in fees.")
    return total_fees 

#This needs to be broken down into other categories.
def spend_points():
    #expenses()
    spend_points = 0
    spend_points = int(input("How many points do you expect to receive from everyday spend?" ))
    print("You expect to earn", spend_points, "points per year.")
    return spend_points

#def expenses():
#    airline_expense = int(input("How is your annual airline expense?" )
#    hotel_expense =
#    other_travel_expense
#    restaurant_expense
#    gas_expense
#    grocerie_expense
#    other_expense
                          

def point_value():
    point_value = 0
    point_value = float(input("In terms of cents per point, how much do you value the points for this credit card?" ))
    point_value = point_value / 100
    print("These points are worth", point_value)
    return point_value

#This would only apply if a card holder is in his/her first year of owning the cards.
def sign_up_bonus():
    receive_bonus = str(input("Will you be receiving a sign up bonus?"))
    if receive_bonus == "yes":
        sign_up_bonus = int(input("How many bonus points will you recieve?" ))
    else:
        sign_up_bonus = 0
    return sign_up_bonus


def card():
    name = input("What is the name of the card?" )
    print('')
    totalCredits = total_credits()
    print('')
    totalFees = total_fees()
    print('')
    spendPoints = spend_points()
    print('')
    pointValue = point_value()
    print('')
    bonusPoints = sign_up_bonus()
    print('')
    expected_value = totalCredits - totalFees + (spendPoints * pointValue) + (bonusPoints * pointValue)
    print("The expected value for the ", name, "card is", str(expected_value),"dollars.")

    
card()

