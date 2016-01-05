FORBIDDEN_CHARS = {105, 108, 111}

def incr(char):
    char -= 97
    char = (char + 1) % 26
    return char + 97

def increment_password(bytestring):
    chars = list(bytestring)
    chars_to_change = 1
    for char in chars[::-1]:
        if char == 122:
            chars_to_change += 1
        else:
            break

    for i in range(chars_to_change):
        j = i+1
        chars[-j] = incr(chars[-j])

    return bytes(chars)
            

def doubles_test(bytestring):
    chars = list(bytestring)
    first_pair = ''
    for idx, char in enumerate(chars):
        if idx + 1 >= len(chars):
            return False
        if char == chars[idx+1]:
            if first_pair == '':
                first_pair = char + chars[idx+1]
                continue
            if char + chars[idx+1] != first_pair:
                return True


def series_test(bytestring):
    chars = list(bytestring)
    for idx, char in enumerate(chars):
        if idx + 2 >= len(chars):
            return False

        if incr(char) == chars[idx+1]:
            if incr(chars[idx+1]) == chars[idx+2]:
                return True

def iol_absent(bytestring):
    chars = list(bytestring)
    for char in chars:
        if char in FORBIDDEN_CHARS:
            return False

    return True

