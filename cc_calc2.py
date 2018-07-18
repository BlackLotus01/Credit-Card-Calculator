def get_value(query):
    question = query + ' ? '
    answer = input(question)
    if answer == '':
        answer = 0
    print(answer)
    return answer

total_credits = get_value("How much in credits did you receive")
total_fees = get_value("How much in fees did you pay (put a negative numbers)")
point_value = get_value("How much are the points worth for this credit card" )
spend_points = get_value("How many points do you expect to receive from everyday spend" )

total_value = 0
total_value = (int(total_credits) + int(total_fees) + (int(spend_points) * float(point_value)))

print(total_value)
