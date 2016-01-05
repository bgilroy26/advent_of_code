import sys

filename = sys.argv[1]

in_routes = []
locations = set()
final_routes = []

with open(filename, 'r') as f:
    for line in f:
        words = line.split(' ')
        route_name = words[0][:3] + '_' + words[2][:3]
        in_routes.append((route_name, int(words[-1])))

    sorted_routes = sorted(in_routes, key=lambda route: route[1])
    print(sorted_routes)
    sys.exit()

    for route in sorted_routes:
        if route[0][:3] not in locations or route[0][4:] not in locations:
            final_routes.append(route)
            locations.add(route[0][:3])
            locations.add(route[0][4:])

    spanning_distance = sum([route[1] for route in final_routes])
    print(final_routes)
    sys.exit()
    print('shortest spanning distance is {0}'.format(spanning_distance))

    


