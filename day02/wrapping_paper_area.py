import Toy_Dimensions 
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

        #first side left out of first area...
        side_areas = [ 
                dims[1]*dims[2],
                dims[0]*dims[2],
                dims[0]*dims[1]
                ]
                        
        ordered_areas = sorted(side_areas)

        total += ordered_areas[0]*3 + ordered_areas[1]*2 + ordered_areas[2]*2
    print("{0:,} square feet of wrapping paper".format(total))
       
