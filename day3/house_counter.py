import sys
import operator

filename = sys.argv[1]

houses = {(0,0)}
santa_location = (0,0)

directional = {
        '^': (0,1),
        '>':(1,0),
        'v':(0,-1),
        '<':(-1,0)
        }

with open(filename, 'r') as f:
    while True:
        char = f.read(1)
        if char == '':
            break

        santa_location = tuple(map(operator.add, santa_location, directional[char]))

        houses.add(santa_location)
        
    total = len(houses)
    print("{0:,} houses".format(total))
 
        
        
        
