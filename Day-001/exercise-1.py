str = 'X_DSPAM-Confidence: 0.8475 '

# Find start position of number
numStart = str.find(' ') + 1
# Find stop position of number
numStop = str.find(' ', numStart)

# Get number string
num = str[numStart:numStop]

# Convert string to float
num = float(num)

# Print number
print(num)