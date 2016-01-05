import sys
assignment_operator = '->'
gates = ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT'] 

'''
class Signal(object):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        value = int(value)
        #wires carry 16 bit signal
        value_range = 65536
        lower = 0
        upper = value_range - 1

        while value > upper:
            value = value - value_range
        while value < lower:
            value = value + value_range
        self._value = value
        
'''

def give_wire(line):
    instruction = line.split(' ')
    return instruction[-1]

def is_numeric_assignment(line):
    gate, index = give_gate(line)
    instruction = line.split(' ')
    return instruction[0].isdigit() and gate == ''

def give_gate(line):
    instruction = line.split(' ')
    index_gate_list = [(ind, word) for ind, word in enumerate(instruction) if word[0].isupper()]
    if not index_gate_list:
        #first item is 'no gate'; second item is 'no index'
        return ('', None)
    index, gate = index_gate_list[0]
    return (''.join(gate), index)

def give_left_right_operands(line, gate_index):
    instruction = line.split(' ')
    left_operand = instruction[ gate_index - 1 ] 
    right_operand = instruction[ gate_index + 1 ] 
    return (left_operand, right_operand)

