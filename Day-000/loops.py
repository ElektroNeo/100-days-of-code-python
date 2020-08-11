n = 5
smallest = None

# Find smallest
for value in [5, 14, 7, 65, -54, 3]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value

# Print 5 times
while n > 0:
    print(smallest)
    n = n - 1