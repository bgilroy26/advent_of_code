import sys
import operator

filename = sys.argv[1]

houses = {(0,0)}
santa_location = (0,0)
robot_location = (0,0)

directional = {
        '^': (0,1),
        '>':(1,0),
        'v':(0,-1),
        '<':(-1,0)
        }

with open(filename, 'r') as f:
    end = f.seek(0,2)

with open(filename, 'r') as f:
    while True:
        santa_char, robo_char = f.read(2)

        santa_location = tuple(map(operator.add, santa_location, directional[santa_char]))
        robot_location = tuple(map(operator.add, robot_location, directional[robo_char]))

        houses.add(santa_location)
        houses.add(robot_location)

        if f.tell() == end:
            break
        
    total = len(houses)
    print("{0:,} houses".format(total))
