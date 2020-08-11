# Get input
x = input('Enter a number: ')

# Check for number
try:
    x = int(x)
except:
    x = -1
x = int(x)

# Print
if x == -1:
    print('Wrong input!!!')
elif x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done!')