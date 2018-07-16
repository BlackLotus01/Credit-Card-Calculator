# Credit-Card-Calculator
# The calculator will take three credit cards and evaluate the best option for a credit card applicant.


point_value = 0
total_fees = 0
total_credit = 0
spend_points = 0

name = ''

# Main program
def card(point_value, total_fees, total_credits, spend_points):
    name = input("What is the name of the card?" )
    total_value = 0
    total_value = int(total_credits) + int(total_fees) + (int(spend_points) * float(point_value))
    print(total_value)

# This will set the value a user believes the credit card points are worth.
def point_value():
    point_value = 0
    point_value = input("How much are the points for this credit card worth?" )
    print("These points are worth", point_value)
    return point_value

# Get the total amount in fees a user will pay annually.
def total_fees():
    total_fees = 0
    annual_fee = int(input("What is the annual fee?" ))
    authorized_users = int(input("What is the total authorized user fee?" ))
    foriegn_fee = int(input("How much do you expect to pay in foriegn transaction fees?" ))
    other_fees = int(input("How much were you charged for all other fees?" ))
    total_fees = annual_fee + authorized_users + foriegn_fee + other_fees
    print("You will pay", str(total_fees), "dollars in fees.")
    return total_fees 

# Get the total amount in credits a user will receive.
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
    
def spend_points():
    spend_points = 0
    spend_points = input(float("How many points do you expect to receive from everyday spend?" ))
    return spend_points

card(point_value, total_fees, total_credits, spend_points)


