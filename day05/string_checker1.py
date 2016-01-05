import sys

filename = sys.argv[1]

naughty_strings = {
        'a':'b',
        'c':'d',
        'p':'q',
        'x':'y',
        '':False
        }

naughty_keys = list(naughty_strings.keys())

vowels = 'aeiou'
last_char = ''

total = 0
print("{0} {1} {2} {3} ".format("line".center(16), "vowel_count", "has_double_letter", "contains_naughty_strings"))

with open(filename, 'r') as f:
    for line in f:
        vowel_count = 0
        has_double_letter = False
        contains_naughty_strings = False

        for char in line:
            if vowel_count < 3:
                if char in vowels:
                    vowel_count += 1

            if not has_double_letter:
                if char == last_char:
                    has_double_letter = True

            if not contains_naughty_strings:
                if last_char in naughty_keys:
                    if naughty_strings[last_char] == char:
                            contains_naughty_strings = True

            if not has_double_letter or not contains_naughty_strings:
                last_char = char
                        
        if vowel_count >= 3 and has_double_letter and not contains_naughty_strings:
            total += 1

        line = line[:-1]
        print('{0} -- {1} | {2} | {3}'.format(line, str(vowel_count).center(11), str(has_double_letter).center(17), str(contains_naughty_strings).center(24)))
    
    print()
    print("{0} nice strings on the list".format(total))



 
