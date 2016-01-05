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

def switch_list_builder(first_light_index, last_light_index):
    initial_non_mods = first_light_index
    terminal_non_mods = 999 - last_light_index
    switch_lights = last_light_index - (first_light_index - 1)
    return [False]*initial_non_mods + [True]*switch_lights + [False]*terminal_non_mods

def turn_off(val):
    if val != 0:
        val -= 1
        return val
    return 0

def turn_on(val):
    val += 1
    return val 

def toggle(val):
    val += 2
    return val
