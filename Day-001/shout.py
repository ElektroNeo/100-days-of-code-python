# Get file name from user
fname = input('Enter a file name: ')

# Check for file existance
try:
    fhand = open(fname)
# Exit program if an error appears
except:
    print('There is not such as file!')
    quit()

# Convert all characters to upper case
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)