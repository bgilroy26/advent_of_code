#from @Stranac Coding on Youtube
import sys
import ast

def all_numbers(data):
    if isinstance(data, int):
        yield data

    if isinstance(data, list):
        for value in data:
            yield from all_numbers(value)

    if isinstance(data, dict):
        if 'red' in data.values():
            return

        for value in data.values():
            yield from all_numbers(value)

def main(text):
    list_x = ast.literal_eval(text)
    
    result = sum(all_numbers(list_x))
    print(result)

if __name__ == '__main__':
    text = sys.stdin.read()
    main(text)
