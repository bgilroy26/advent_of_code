import Toy_Dimensions 
from functools import reduce
import operator
import sys

filename = sys.argv[1]
total = 0

with open(filename, 'r') as f:
    end = f.seek(0,2)

with open(filename, 'r') as f:
    while True:
        if f.tell() == end:
            break

        dims = Toy_Dimensions.get_dims(f.readline())

        sorted_dims = sorted(list(dims))

        smallest_side_area = 2*sorted_dims[0] + 2*sorted_dims[1] 
        volume = reduce(operator.mul, dims)
        total += smallest_side_area + volume

    print("{0:,} feet of ribbon".format(total))
