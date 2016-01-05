import sys

filename = sys.argv[1]

two_chars_ago = ''
last_char = ''

total = 0

#New rules are:
#  - palindromic triple
#  - doubled pair

candidate_pairs = []

print("{0} {1} {2} ".format("line".center(16), "has_palindromic_triple", "has_doubled_pair"))

with open(filename, 'r') as f:
    for line in f:
        has_palindromic_triple = False
        has_doubled_pair = False

        for char in line:
            if not has_palindromic_triple:
                if char == two_chars_ago:
                    has_palindromic_triple = True

            if last_char != '' and line.count(last_char + char) > 1:
                has_doubled_pair = True

            if not has_palindromic_triple or not has_doubled_pair:
                two_chars_ago = last_char
                last_char = char
                        
        if has_palindromic_triple and has_doubled_pair:
            total += 1

        line = line[:-1]
        print('{0} -- {1} | {2} '.format(line, str(has_palindromic_triple).center(22), str(has_doubled_pair).center(16)))
    
    print()
    print("{0} nice strings on the list".format(total))

