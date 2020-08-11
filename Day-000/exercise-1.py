hour = input('Enter hours: ')

try:
    hour = float(hour)
except :
    hour = -1.0

rate = input('Enter rate: ')

try:
    rate = float(rate)
except :
    rate = -1.0

if hour == -1.0 or rate == -1.0:
    print('Error, please enter numeric input')
elif hour > 40:
    print('Pay: ' + str((40*rate)+((hour-40)*rate*1.5)))
else:
    print('Pay: ' + str(hour*rate))
    