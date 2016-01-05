import sys
from ElfTranslate import elf_translate


def main(times, data):

    for i in range(int(times)):
        #print()
        #print('data: ', data)
        data = elf_translate(data)

    return data
        

if __name__ == '__main__':
   times = sys.argv[1]
   data = sys.stdin.readline()
   print(main(times, data))

