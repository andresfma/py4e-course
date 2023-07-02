hoursstr = input("Enter number of hours: ")
ratestr = input("Enter rate: ")


def computepay() :
    hours = float(hoursstr)
    rate = float(ratestr)

    if hours < 40 :
        pay = hours*rate
    elif hours > 40 :
        pay = 40*rate + 1.5*rate*(hours-40)
    return pay

print("Pay", computepay())