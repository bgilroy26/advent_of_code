import sys
import CircuitBookletReader
assignment_operator = '->'
gates = ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT'] 

class SignalTree():
    def __init__(self, root):
        self.root = Signal(root)
        self.next_node = None
        self.current_last_leaf = self.root
    
    def add(name):
        self.current_last_leaf.next_node = Signal(name)
        self.current_last_leaf = current_last_leaf.next_node

    def find_last_leaf(self):
        node = self.root
        while True:
            if node.next_node is None:
                return node
            else:
                node = node.next_node

class Signal(object):
    def __init__(self, name):
        self.name = name
        self.operands = []
        
    def get_operands(instruction):
        self.instruction_gate, index = CircuitBookletReader.give_gate(line)
        words = instruction.split(' ')
        if gate == '':
            self.operands.append(words[0])


                '''
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
'''

