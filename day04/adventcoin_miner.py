import hashlib

candidate = 282749

while True:
    m = hashlib.md5()

    test = 'yzbqklnj' + str(candidate)
    

    m.update(test.encode('utf-8'))

    test_hex = m.hexdigest()[:6]

    if test_hex == '000000':
        break
    candidate += 1

print(test)

