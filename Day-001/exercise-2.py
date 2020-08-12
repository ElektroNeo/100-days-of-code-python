# Get file name from user
fname = input('Enter a file name: ')

# Check for file existance
try:
    fhand = open(fname)
# Exit program if an error appears
except:
    print('There is not such as file!')
    quit()

# Create empty dictionary
counts = dict()

# Make histogram of words
for line in fhand:
    # Split every lines
    words = line.split()
    # Count number of word usage
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Create empty variables
bigCount = None
bigWord = None

# Find most used word
for (word,count) in counts.items():
    if bigCount is None or bigCount < count:
        bigCount = count
        bigWord = word

# Print most used word and its count
print('The most used word: ', bigWord)
print('Number of usage: ', bigCount)