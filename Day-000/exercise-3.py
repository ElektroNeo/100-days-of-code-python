# Initialise variables
total = 0
count = 0
avarage = 0

# Loop until user enters 'done'
while True:
    # Get input
    num = input('Enter a number: ')

    # If user enters done, then print total, count, avarege end break loop
    if num == 'done':
        print(total, count, total/count)
        break
    # If user enters number
    else:
        # Check for number
        try:
            num = int(num)
        # If fails print 'Invalid number' and continue
        except:
            print('Invalid input!')
            continue
        # Increase count
        count = count + 1
        # Add num to total
        total = total + num