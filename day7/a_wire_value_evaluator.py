import sys
import pprint
import operator
import CircuitBookletReader

filename = sys.argv[1]
wire_signals = {}
wire_name = ''
gate = ''
left_operand = ''
right_operand = ''
final_instructions = []
lines_to_delete = []

def process_line(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            words = line.split(' ')
            wire_name = CircuitBookletReader.give_wire(line)
            gate, index = CircuitBookletReader.give_gate(line)
            if gate == '':
                wire_signals[wire_name] = CircuitBookletReader.Signal(words[0])
            if gate == 'NOT':
                if wire_name in list(wire_signals.keys()):
                    wire_signals[wire_name].value = ~wire_signals[words[1]]
                else:
                    wire_signals[wire_name] = CircuitBookletReader.Signal(~wire_signals[words[1]])
            if gate == 'OR':
                if wire_name in list(wire_signals.keys()):
                    wire_signals[wire_name].value = wire_signals[words[0]] | wire_signals[words[2]]
                else:
                    wire_signals[wire_name] = CircuitBookletReader.Signal(wire_signals[words[0]] | wire_signals[words[2]])
            if gate == 'AND':
                if wire_name in list(wire_signals.keys()):
                    wire_signals[wire_name].value = wire_signals[words[0]] & wire_signals[words[2]]
                else:
                    wire_signals[wire_name] = CircuitBookletReader.Signal(wire_signals[words[0]] & wire_signals[words[2]])
            if gate == 'lshift':
                if wire_name in list(wire_signals.keys()):
                    wire_signals[wire_name].value = operator.lshift(wire_signals[words[0]], int(words[2]))
                else:
                    wire_signals[wire_name] = CircuitBookletReader.Signal(operator.lshift(wire_signals[words[0]], int(words[2])))
            if gate == 'RSHIFT':
                if wire_name in list(wire_signals.keys()):
                    wire_signals[wire_name].value = operator.rshift(wire_signals[words[0]], int(words[2]))
                else:
                    wire_signals[wire_name] = CircuitBookletReader.Signal(operator.rshift(wire_signals[words[0]], int(words[2])))

        pprint.pprint(wire_signals,indent=4)

def main():
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        
        #first pass -- Move numeric direct assignments to the top
        for line_index, line in enumerate(lines):
            if  CircuitBookletReader.is_numeric_assignment(line):
                final_instructions.append(line)
                lines_to_delete.append(line_index)
                
        new_instructions = [instruction for inst_ind, instruction in enumerate(lines) if inst_ind not in lines_to_delete] 
        lines_to_delete = []

        print(new_instructions)
        i = 0
        while(True):
            print(i)
            i += 1
            if i == 100:
                break
            #get wires
            defined_wires = [CircuitBookletReader.give_wire(inst) for inst in final_instructions]
            if i == 99:
                print(defined_wires)

            #second pass -- okay to move lines with only direct assignments on the left
            for line_index2, line2 in enumerate(new_instructions):
                gate, gate_index = CircuitBookletReader.give_gate(line2)
                if gate_index is None:
                   lefthand = line2[0] 
                   if lefthand in defined_wires:
                       final_instructions.append(line2)
                       lines_to_delete.append([line_index2])
                elif gate == 'AND' or gate == 'OR':
                    left_op, right_op = CircuitBookletReader.give_left_right_operands(line2, gate_index)
                    if left_op in defined_wires and right_op in defined_wires:
                        final_instructions.append(line2)
                        lines_to_delete.append([line_index2])
                elif gate[1:] == 'SHIFT':
                    left_op = line2[0]
                    if left_op in defined_wires:
                        final_instructions.append(line2)
                        lines_to_delete.append([line_index2])

            new_instructions = [instruction for inst_ind, instruction in enumerate(new_instructions) if inst_ind not in lines_to_delete] 
            print(len(new_instructions))
            sys.exit()
            lines_to_delete = []

    print(len(new_instructions))
    print(len(final_instructions))
    #print(wire_signals['a'])

if __name__ == '__main__':
    process_line(filename)
