import re

# Get file name
fname = input('Enter a file name: ')

# Check file
try:
    fhand = open(fname)
except:
    print('Something wrong!')
    quit()

# Create empty dictionary for word count
d = dict()

# Count words
for line in fhand:
    # Use reqular expression to word without punctiations
    words = re.findall('[A-Za-z]+', line)
    for word in words:
        d[word] = d.get(word, 0) + 1

# Create empty list for sorted word count
l = list()

# Sort word by count
l = sorted([(v,k) for (k,v) in d.items()], reverse=True)

# Print first 3 most used words
for v,k in l[:3]:
    print(k,v)


