ADDRESS_LENGTH = 3
COMMA_LENGTH = 1

def find_command(line):
    instructions_tuple = (
            'turnoff',
            'turnon',
            'toggle'
            )

    instructions = line.split(' ')
    if instructions[0] in instructions_tuple:
        return 2
    if instructions[0] + instructions[1] == instructions_tuple[1]:
        return 1
    return 0

def get_indices(line):
    instructions = line.split(' ')
    if instructions[0] == 'turn':
        first_address = instructions[2]
        second_address = instructions[4]
    else:
        first_address = instructions[1]
        second_address = instructions[3]
    first_index_location = first_address.find(',') + COMMA_LENGTH
    first_index = first_address[first_index_location:]
    second_index_location = second_address.find(',') + COMMA_LENGTH
    second_index = second_address[second_index_location:]
    return (int(first_index), int(second_index))

def get_rows(line):
    instructions = line.split(' ')
    if instructions[0] == 'turn':
        first_address = instructions[2]
        second_address = instructions[4]
    else:
        first_address = instructions[1]
        second_address = instructions[3]
    first_comma_location = first_address.find(',')
    first_row = first_address[0:first_comma_location]
    second_comma_location = second_address.find(',')
    second_row = second_address[0:second_comma_location]
    return (int(first_row), int(second_row))


#to 'AND' with
def turn_off_string(first_light_index, last_light_index):
    initial_ones_count = first_light_index
    terminal_ones_count = 999 - last_light_index 
    middle_zeros = last_light_index - (first_light_index - 1)
    return '1'*initial_ones_count + '0'*middle_zeros + '1'*terminal_ones_count

#to 'OR' with
def turn_on_string(first_light_index, last_light_index):
    initial_zeros_count = first_light_index
    terminal_zeros_count = 999 - last_light_index 
    middle_ones = last_light_index - (first_light_index - 1)
    return '0'*initial_zeros_count + '1'*middle_ones + '0'*terminal_zeros_count
    

#to 'XOR' with
def toggle_string(first_light_index, last_light_index):
    initial_ones_count = first_light_index
    terminal_ones_count = 999 - last_light_index 
    middle_zeros = last_light_index - (first_light_index - 1)
    return '0'*initial_ones_count + '1'*middle_zeros + '0'*terminal_ones_count

def turn_off(bits, bit_string):
    result = int(bits, 2) & int(bit_string, 2)
    bin_result = bin(result)[2:]
    return "{0:0>1000}".format(bin_result)

def turn_on(bits, bit_string):
    result = int(bits, 2) | int(bit_string, 2)
    bin_result = bin(result)[2:]
    return "{0:0>1000}".format(bin_result)

def toggle(bits, bit_string):
    result = int(bits, 2) ^ int(bit_string, 2)
    bin_result = bin(result)[2:]
    return "{0:0>1000}".format(bin_result)

