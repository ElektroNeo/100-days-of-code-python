import urllib.request, urllib.parse, urllib.error

# Get data
fhand = urllib.request.urlopen('https://www.w3.org/TR/PNG/iso_8859-1.txt')

# Count words
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# Print counted words
print(counts)