import sys
import DecimalLights

filename = sys.argv[1]
total = 0 

lights = [[0]*1000 for i in range(1000)]

brightness_operations = (
            DecimalLights.turn_off,
            DecimalLights.turn_on,
            DecimalLights.toggle,
            )

with open(filename, 'r') as f:
    for line in f:
        which_op = brightness_operations[DecimalLights.find_command(line)]
        rows = DecimalLights.get_rows(line)
        switch_list = DecimalLights.switch_list_builder(*DecimalLights.get_indices(line))
        lights = [lst if rows[0] > outer_ind or rows[1] < outer_ind else [val if not switch_list[inner_ind] else which_op(val) for inner_ind, val in enumerate(lst)] for outer_ind, lst in enumerate(lights)]

for lst in lights:                        
    total += sum(lst)

print(total)
