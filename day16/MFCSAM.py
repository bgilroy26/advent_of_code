import pprint
import sys
import demjson

true_aunt_stats = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

with sys.stdin as f:
    aunt_data = f.readlines()

aunts = {}
for aunt_desc in aunt_data:
    words = aunt_desc.split(' ')
    aunt_name = "{0}_{1}".format(words[0], words[1][:-1])
    words = words[2:]
    words.insert(0, '{')
    words.append('}')
    aunt_dict_string = ''.join(words)

    aunts[aunt_name] = demjson.decode(aunt_dict_string)

pprint.pprint(aunts)



