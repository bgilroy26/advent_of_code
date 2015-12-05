import sys

filename = sys.argv[1]

def alert_santa_floor(filename, floor):
    total = 0

    with open(filename, 'r') as f:
        while True:
            char = f.read(1)
            if char == '(':
                total += 1
            if char == ')':
                total -= 1
            if total == -1:
                break

        position = f.tell()

    return position

if __name__ == '__main__':
    print(alert_santa_floor(filename, -1))
