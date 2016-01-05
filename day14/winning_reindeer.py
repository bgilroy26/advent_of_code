import sys
import pprint
from reindeer import Reindeer

reindeer = []
lines = sys.stdin.readlines()
SECONDS = int(sys.argv[1])

for line in lines:
    words = line.split(' ')
    this_reindeer_attrs = []
    this_reindeer_attrs.append(words[0])
    [this_reindeer_attrs.append(int(word)) for word in words if word.isdigit()]
    reindeer.append(Reindeer(*this_reindeer_attrs))


for i in range(SECONDS):
    j = i+1
    for reindeer_k in reindeer:
        reindeer_k.run(j)
    
    the_field = sorted(reindeer, key=lambda deer: deer.distance, reverse=True)
    furthest = the_field[0]

    [setattr(deer, 'points', deer.points+1) for deer in reindeer if deer.name == furthest.name]
    print(furthest.name, furthest.points)
for deer in reindeer:
    pprint.pprint(deer.__dict__)



