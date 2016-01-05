import sys
import re

with sys.stdin as f:
    text = f.read()

print("sum of all numbers: ", sum(map(int, re.findall("-?[0-9]+", text))))

def sum_all_nums(text):
    return_val = sum(map(int, re.findall("-?[0-9]+", text)))
    return return_val



