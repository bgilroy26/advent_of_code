import sys
import BinaryLights

filename = sys.argv[1]
total = 0 

lights = ['0'*1000 for i in range(1000)]

string_builder_functions = (
            BinaryLights.turn_off_string,
            BinaryLights.turn_on_string,
            BinaryLights.toggle_string,
            )

bitwise_operations = (
            BinaryLights.turn_off,
            BinaryLights.turn_on,
            BinaryLights.toggle,
            )

with open(filename, 'r') as f:
    for line in f:
        which_op = BinaryLights.find_command(line)
        rows = BinaryLights.get_rows(line)
        bit_string = string_builder_functions[which_op](*BinaryLights.get_indices(line))
        #SO 13628791 for between; SO 14864922 for list comp with index; SO 2582138 for processing some of list
        lights = [bits if rows[0] > ind or rows[1] < ind else bitwise_operations[which_op](bits, bit_string) for ind, bits in enumerate(lights)]

#SO 9829578 for 1 counting
for row in lights:
    total += row.count("1")

print("{0} lights are on".format(total))
    
