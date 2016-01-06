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

def mfcsam_test(key, true_aunt_stat, aunt_trait):
    #retro-encabulator
    higher = ['cats', 'trees']
    lower = ['pomeranians', 'goldfish']
    if key in higher:
        return true_aunt_stat > aunt_trait
    if key in lower:
        return true_aunt_stat < aunt_trait
    return true_aunt_stat != aunt_trait

with sys.stdin as f:
    aunt_data = f.readlines()

aunts = {}
aunts_with_potential = []

for aunt_desc in aunt_data:
    words = aunt_desc.split(' ')
    aunt_name = "{0}_{1}".format(words[0], words[1][:-1])
    words = words[2:]
    words.insert(0, '{')
    words.append('}')
    aunt_dict_string = ''.join(words)

    aunts[aunt_name] = demjson.decode(aunt_dict_string)

for name, aunt in aunts.items():
    for key, aunt_trait in aunt.items():
        not_aunt = False
        if mfcsam_test(key, true_aunt_stats[key], aunt_trait):
            not_aunt = True
            break
            
    
    if not not_aunt:
        aunts_with_potential.append(name)

pprint.pprint(aunts_with_potential)
