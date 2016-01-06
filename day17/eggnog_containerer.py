import sys
import pprint
import itertools

with sys.stdin as f:
    str_size_list = f.readlines()

size_list = map(int, str_size_list)
appropriate_combos = []

#SO 18035595
def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

for result in powerset(size_list):
    if sum(result) == 150 and len(result) == 4:
        appropriate_combos.append(result)
 
pprint.pprint(appropriate_combos)
print(len(appropriate_combos))
