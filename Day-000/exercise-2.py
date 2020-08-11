# Compute pay function
def computepay(hours, rate):
    try:
        hour = float(hours)
    except :
        hour = -1.0
    try:
        rate = float(rate)
    except :
        rate = -1.0

    if hour == -1.0 or rate == -1.0:
        return -1
    elif hour > 40:
        return (40*rate)+((hour-40)*rate*1.5)
    else:
        return hour*rate
    
# Get hours and rate
h = input('Enter hours: ')
r = input('Enter rate: ')

# Calculate pay
pay = computepay(h, r)

# Print pay if exist
if pay == -1:
    print('Error, please enter numeric input')
else:
    print('Pay: ' , pay)




    