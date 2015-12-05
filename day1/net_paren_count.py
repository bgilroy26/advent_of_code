import sys

filename = sys.argv[1]
total = 0

with open(filename, 'r') as f:
    char = f.read(1)
    while char != '':
        if char == '(':
            total += 1
        if char == ')':
            total -= 1

        char = f.read(1)
    print(total)




