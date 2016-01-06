import pprint
import sys
import collections
import functools
import operator

product = functools.partial(functools.reduce, operator.mul)

def tryint(x):
    try:
        return int(x)
    except ValueError:
        return x

# initialize ingredients (e.g. chocolate, butterscotch...) with their 
# respective stats
ingredients = ['Butterscotch', 'Candy', 'Chocolate', 'Sprinkles']
stats = ['capacity', 'durability', 'flavor', 'texture', 'calories']
ingredient_data = collections.defaultdict(dict)

#filename = input('please type filename and press enter ')
filename = 'input.txt'

with open(filename, 'r') as f:
    for i in range(len(ingredients)):
        j = range(5)
        j = iter(j)
        desc = f.readline()
        desc_words = desc.split(' ')
        for word in desc_words:
            if word[-1] ==',':
                word = word[:-1]
            word = tryint(word)
            if isinstance(word, int):
                x = next(j)
                ingredient_data[ingredients[i]][stats[x]] = int(word)



#generates all vectors [m, n, o, p] where m+n+o+p is less than 100
#max deliciousness variable holds the cookie product and the 
#teaspoons vector that is winning so far
teaspoons = [[m,n,o,p] for m in range(100) for n in range(100) for o in range(100) for p in range(100) if m+n+o+p == 100]

max_deliciousness = (
        0, [0,0]
        )

#for stat in stats:
#    cookie_stats[stat] = 0

#multiply stats by teaspoon per ingredient and combine
for t_4 in teaspoons:
    cookie_stats = collections.defaultdict(int)
    for ingredient_index in range(4):
        for stat in stats:
            ingredient = ingredients[ingredient_index]
            cookie_stats[stat] += t_4[ingredient_index]*ingredient_data[ingredient][stat]

    if all(stat > 0 for stat in cookie_stats.values()):
        total = product(value for key, value in cookie_stats.items() if key != 'calories')
        if cookie_stats['calories'] == 500 and total > max_deliciousness[0]:
            max_deliciousness = tuple()
            max_deliciousness = (total, t_4)

pprint.pprint(max_deliciousness)    
