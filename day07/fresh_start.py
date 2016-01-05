import sys
import CircuitBookletReader
import CircuitBookletReader2

counter = 0
twice = False
wires_of_interest = []
wires_of_interest.append(sys.argv[1])
filename = sys.argv[2]
#outfile = sys.argv[3]
signal_tree = SignalTree(wire_of_interest)

#list of two lists:
# first list holds depth,
# second list holds breadth
while True:
    #with open(outfile, 'r') as check_outfile:
        #lines = check_outfile.read().splitlines()
    #true check:
    #if lines[-1][0].isdigit():
    #current check:
    if twice:
        print(signal_tree.find_last_leaf())
        sys.exit
        
    with open(filename, 'r') as instruction_f:
        lines = instruction_f.read().splitlines()
        for line in lines:
            words = line.split(' ')
            wire_name = CircuitBookletReader.give_wire(line)
            if wire_name == wire_of_interest:
                signal_tree.add(line[-1])
                last_leaf = signal_tree.find_last_leaf()
                last_leaf.get_operands(line)


                #print_wire = open(outfile, 'a')
                #print_wire.write(line)
